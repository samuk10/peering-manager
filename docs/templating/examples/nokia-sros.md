# Nokia SR OS

```no-highlight
{% macro bgp_group(group_name,family,parent) %}
group {{ group_name }} {
  type external
  multipath
  advertise-inactive
{%- if parent | iter_import_policies %}
  import policy [ {{ parent | iter_import_policies('slug') | join(' ') }} ]
{%- endif %}
  family ipv{{ '6' if family == 6 else '4' }} true
{%- if parent | iter_export_policies %}
  export policy [ {{ parent | iter_export_policies('slug') | join(' ') }} ]
{%- endif %}
}
{% endmacro %}
{% macro bgp_neighbor(group,family,session) %}
neighbor {{ session | ip }} {
  group {{ group }}
  peer-as {{ session.autonomous_system.asn }}
  {%- if not session.enabled %}
  admin-state disable
  {%- endif %}
  description "Peering: AS{{ session.autonomous_system.asn }} - {{ session.autonomous_system.name }}"
  {%- if family == 6 and session.autonomous_system.ipv6_max_prefixes > 0 %}
  prefix-limit ipv6 maximum {{ session.autonomous_system.ipv6_max_prefixes }}
  {%- endif %}
  {%- if family == 4 and session.autonomous_system.ipv4_max_prefixes > 0 %}
  prefix-limit ipv4 maximum {{ session.autonomous_system.ipv4_max_prefixes }}
  {%- endif %}
  {%- if session | iter_import_policies %}
  import policy [ {{ session | iter_import_policies('slug') | join(' ') }} ]
  {%- endif %}
  {%- if session | iter_export_policies %}
  export policy [ {{ session | iter_export_policies('slug') | join(' ') }} ]-
  {%- endif %}
  {%- if session.encrypted_password %}
  authentication-key "{{ session.encrypted_password }}" custom
  {%- elif session.password %}
  authentication-key "{{ session.password }}"
  {%- endif %}
}
{% endmacro %}
{# Configure custom aes256 encryption algorithm for passwords #}
/admin system security hash-control custom-hash algorithm aes256 key "09123456789012345678901234567890"
/configure router bgp
{%- for ixp in internet_exchange_points %}
  {%- for family in (6, 4) %}
    {%- set group_name = "ipv" + family|string + "-" + ixp.slug %}
    {{ bgp_group(group_name,family,ixp) }}
    {%- for session in router | ixp_sessions(family=family, ixp=ixp) %}
    {{ bgp_neighbor(group_name,family,session) }}
    {%- endfor %}
  {%- endfor %}
{%- endfor %}
{%- for group in bgp_groups %}
  {%- for family in (6, 4) %}
    {%- set group_name = "ipv" + family|string + "-" + group.slug %}
    {{ bgp_group(group_name,family,group) }}
    {%- for session in router | direct_sessions(family=family, group=group)  %}
    {{ bgp_neighbor(group_name,family,session) }}
    {%- endfor %}
  {%- endfor %}
{%- endfor %}
/configure policy-options {
{%- for c in communities %}
    community {{ c.name }} member {{ c.value }}
{%- endfor %}
}
```
