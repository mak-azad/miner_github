import re

def extract_host_info(xml_content):
    pattern = re.compile(r'<host name="(.+?)" ipv4="(.+?)"/>')
    matches = pattern.findall(xml_content)
    
    host_info = []
    for match in matches:
        hostname = match[0]
        ip_address = match[1]
        host_info.append(f"{ip_address}")
    
    return host_info

# Example XML content
xml_content = '''
<rspec xmlns="http://www.geni.net/resources/rspec/3" xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" xmlns:tour="http://www.protogeni.net/resources/rspec/ext/apt-tour/1" xmlns:jacks="http://www.protogeni.net/resources/rspec/ext/jacks/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.geni.net/resources/rspec/3    http://www.geni.net/resources/rspec/3/request.xsd" type="request">
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node0" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1041" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808166">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node0:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1041:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808193" mac_address="1458d058cfc3">
      <ip address="10.10.1.1" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1041" hardware_type="m510"/>
    <host name="node0.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.156"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1041.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node1" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1325" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808070">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node1:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1325:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808194" mac_address="ecb1d7856ac3">
      <ip address="10.10.1.2" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1325" hardware_type="m510"/>
    <host name="node1.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.19"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1325.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node2" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1108" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808113">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node2:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1108:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808195" mac_address="1458d0581f63">
      <ip address="10.10.1.3" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1108" hardware_type="m510"/>
    <host name="node2.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.168"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1108.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node3" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0933" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808172">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node3:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0933:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808196" mac_address="ecb1d7854a63">
      <ip address="10.10.1.4" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0933" hardware_type="m510"/>
    <host name="node3.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.103"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0933.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node4" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0931" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808152">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node4:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0931:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808197" mac_address="1458d058cfb3">
      <ip address="10.10.1.5" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0931" hardware_type="m510"/>
    <host name="node4.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.101"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0931.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node5" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1308" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808160">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node5:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1308:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808198" mac_address="1458d0583f33">
      <ip address="10.10.1.6" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1308" hardware_type="m510"/>
    <host name="node5.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.2"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1308.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node6" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0907" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808133">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node6:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0907:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808199" mac_address="ecb1d7850a63">
      <ip address="10.10.1.7" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0907" hardware_type="m510"/>
    <host name="node6.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.77"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0907.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node7" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0904" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808180">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node7:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0904:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808200" mac_address="1458d058efb3">
      <ip address="10.10.1.8" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0904" hardware_type="m510"/>
    <host name="node7.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.74"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0904.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node8" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0837" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808158">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node8:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0837:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808201" mac_address="ecb1d7855a53">
      <ip address="10.10.1.9" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0837" hardware_type="m510"/>
    <host name="node8.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.62"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0837.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node9" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1303" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808169">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node9:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1303:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808202" mac_address="1458d058ff63">
      <ip address="10.10.1.10" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1303" hardware_type="m510"/>
    <host name="node9.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.253"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1303.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node10" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0909" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808121">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node10:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0909:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808203" mac_address="1458d0580f43">
      <ip address="10.10.1.11" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0909" hardware_type="m510"/>
    <host name="node10.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.79"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0909.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node11" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1342" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808162">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node11:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1342:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808204" mac_address="ecb1d7852a43">
      <ip address="10.10.1.12" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1342" hardware_type="m510"/>
    <host name="node11.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.36"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1342.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node12" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1305" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808145">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node12:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1305:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808205" mac_address="1458d0583fc3">
      <ip address="10.10.1.13" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1305" hardware_type="m510"/>
    <host name="node12.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.255"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1305.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node13" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0823" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808073">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node13:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0823:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808206" mac_address="ecb1d7856a33">
      <ip address="10.10.1.14" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0823" hardware_type="m510"/>
    <host name="node13.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.48"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0823.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node14" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0813" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808119">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node14:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0813:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808207" mac_address="1458d0585fd3">
      <ip address="10.10.1.15" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0813" hardware_type="m510"/>
    <host name="node14.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.38"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0813.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node15" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1327" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808157">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node15:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1327:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808208" mac_address="ecb1d7852a73">
      <ip address="10.10.1.16" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1327" hardware_type="m510"/>
    <host name="node15.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.21"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1327.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node16" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1232" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808155">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node16:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1232:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808209" mac_address="1458d058fed3">
      <ip address="10.10.1.17" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1232" hardware_type="m510"/>
    <host name="node16.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.237"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1232.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node17" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0915" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808035">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node17:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0915:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808210" mac_address="1458d0587fe3">
      <ip address="10.10.1.18" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0915" hardware_type="m510"/>
    <host name="node17.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.85"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0915.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node18" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1033" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808047">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node18:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1033:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808211" mac_address="1458d058bfa3">
      <ip address="10.10.1.19" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1033" hardware_type="m510"/>
    <host name="node18.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.148"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1033.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node19" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1341" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808138">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node19:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1341:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808212" mac_address="1458d058ffd3">
      <ip address="10.10.1.20" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1341" hardware_type="m510"/>
    <host name="node19.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.35"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1341.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node20" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1331" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808054">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node20:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1331:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808213" mac_address="1458d0581fa3">
      <ip address="10.10.1.21" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1331" hardware_type="m510"/>
    <host name="node20.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.25"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1331.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node21" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1209" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808112">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node21:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1209:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808214" mac_address="1458d0582f03">
      <ip address="10.10.1.22" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1209" hardware_type="m510"/>
    <host name="node21.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.214"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1209.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node22" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1002" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808147">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node22:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1002:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808215" mac_address="ecb1d7853a93">
      <ip address="10.10.1.23" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1002" hardware_type="m510"/>
    <host name="node22.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.117"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1002.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node23" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1233" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808154">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node23:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1233:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808216" mac_address="ecb1d7855ab3">
      <ip address="10.10.1.24" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1233" hardware_type="m510"/>
    <host name="node23.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.238"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1233.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node24" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1336" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808144">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node24:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1336:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808217" mac_address="1458d058ffc3">
      <ip address="10.10.1.25" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1336" hardware_type="m510"/>
    <host name="node24.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.30"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1336.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node25" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0826" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808141">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node25:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0826:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808218" mac_address="1458d058ef23">
      <ip address="10.10.1.26" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0826" hardware_type="m510"/>
    <host name="node25.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.51"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0826.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node26" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1214" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808167">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node26:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1214:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808219" mac_address="ecb1d7850a83">
      <ip address="10.10.1.27" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1214" hardware_type="m510"/>
    <host name="node26.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.219"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1214.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node27" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0923" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808151">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node27:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0923:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808220" mac_address="ecb1d7853a03">
      <ip address="10.10.1.28" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0923" hardware_type="m510"/>
    <host name="node27.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.93"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0923.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node28" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1031" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808068">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node28:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1031:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808221" mac_address="1458d0583fa3">
      <ip address="10.10.1.29" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1031" hardware_type="m510"/>
    <host name="node28.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.146"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1031.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node29" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0918" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808105">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node29:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0918:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808222" mac_address="1458d0582fb3">
      <ip address="10.10.1.30" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0918" hardware_type="m510"/>
    <host name="node29.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.88"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0918.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node30" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0935" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808148">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node30:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0935:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808223" mac_address="ecb1d785ea93">
      <ip address="10.10.1.31" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0935" hardware_type="m510"/>
    <host name="node30.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.105"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0935.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node31" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1004" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808040">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node31:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1004:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808224" mac_address="1458d0585f83">
      <ip address="10.10.1.32" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1004" hardware_type="m510"/>
    <host name="node31.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.119"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1004.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node32" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1022" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808069">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node32:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1022:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808225" mac_address="1458d058cec3">
      <ip address="10.10.1.33" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1022" hardware_type="m510"/>
    <host name="node32.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.137"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1022.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node33" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1227" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808083">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node33:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1227:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808226" mac_address="ecb1d7850a03">
      <ip address="10.10.1.34" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1227" hardware_type="m510"/>
    <host name="node33.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.232"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1227.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node34" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0930" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808179">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node34:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0930:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808227" mac_address="1458d058af03">
      <ip address="10.10.1.35" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0930" hardware_type="m510"/>
    <host name="node34.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.100"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0930.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node35" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0802" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808153">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node35:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0802:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808228" mac_address="ecb1d7853ab3">
      <ip address="10.10.1.36" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0802" hardware_type="m510"/>
    <host name="node35.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.27"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0802.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node36" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0827" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808134">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node36:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0827:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808229" mac_address="1458d058bff3">
      <ip address="10.10.1.37" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0827" hardware_type="m510"/>
    <host name="node36.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.52"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0827.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node37" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1306" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808058">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node37:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1306:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808230" mac_address="ecb1d7852a53">
      <ip address="10.10.1.38" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1306" hardware_type="m510"/>
    <host name="node37.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.0"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1306.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node38" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1114" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808042">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node38:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1114:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808231" mac_address="1458d058eed3">
      <ip address="10.10.1.39" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1114" hardware_type="m510"/>
    <host name="node38.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.174"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1114.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node39" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1326" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808165">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node39:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1326:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808232" mac_address="1458d0585fb3">
      <ip address="10.10.1.40" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1326" hardware_type="m510"/>
    <host name="node39.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.20"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1326.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node40" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1335" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808048">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node40:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1335:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808233" mac_address="ecb1d7855aa3">
      <ip address="10.10.1.41" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1335" hardware_type="m510"/>
    <host name="node40.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.29"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1335.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node41" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1312" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808186">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node41:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1312:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808234" mac_address="1458d0588f53">
      <ip address="10.10.1.42" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1312" hardware_type="m510"/>
    <host name="node41.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.6"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1312.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node42" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1119" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808092">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node42:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1119:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808235" mac_address="1458d058dfe3">
      <ip address="10.10.1.43" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1119" hardware_type="m510"/>
    <host name="node42.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.179"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1119.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node43" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1224" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808034">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node43:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1224:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808236" mac_address="1458d0584f53">
      <ip address="10.10.1.44" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1224" hardware_type="m510"/>
    <host name="node43.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.229"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1224.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node44" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1003" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808146">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node44:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1003:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808237" mac_address="1458d0586f53">
      <ip address="10.10.1.45" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1003" hardware_type="m510"/>
    <host name="node44.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.118"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1003.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node45" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1309" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808031">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node45:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1309:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808238" mac_address="ecb1d7857a33">
      <ip address="10.10.1.46" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1309" hardware_type="m510"/>
    <host name="node45.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.3"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1309.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node46" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1240" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808093">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node46:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1240:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808239" mac_address="ecb1d7852ab3">
      <ip address="10.10.1.47" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1240" hardware_type="m510"/>
    <host name="node46.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.245"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1240.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node47" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1223" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808128">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node47:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1223:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808240" mac_address="1458d0584fe3">
      <ip address="10.10.1.48" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1223" hardware_type="m510"/>
    <host name="node47.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.228"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1223.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node48" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1230" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808183">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node48:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1230:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808241" mac_address="1458d0587f73">
      <ip address="10.10.1.49" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1230" hardware_type="m510"/>
    <host name="node48.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.235"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1230.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node49" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1208" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808079">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node49:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1208:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808242" mac_address="1458d058fe83">
      <ip address="10.10.1.50" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1208" hardware_type="m510"/>
    <host name="node49.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.213"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1208.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node50" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0801" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808171">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node50:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0801:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808243" mac_address="1458d058eea3">
      <ip address="10.10.1.51" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0801" hardware_type="m510"/>
    <host name="node50.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.26"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0801.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node51" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1323" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808052">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node51:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1323:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808244" mac_address="1458d0588fe3">
      <ip address="10.10.1.52" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1323" hardware_type="m510"/>
    <host name="node51.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.17"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1323.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node52" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0940" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808104">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node52:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0940:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808245" mac_address="ecb1d7851a13">
      <ip address="10.10.1.53" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0940" hardware_type="m510"/>
    <host name="node52.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.110"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0940.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node53" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0913" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808097">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node53:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0913:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808246" mac_address="1458d058ff13">
      <ip address="10.10.1.54" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0913" hardware_type="m510"/>
    <host name="node53.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.83"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0913.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node54" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1205" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808067">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node54:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1205:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808247" mac_address="ecb1d7852ac3">
      <ip address="10.10.1.55" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1205" hardware_type="m510"/>
    <host name="node54.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.210"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1205.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node55" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1338" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808086">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node55:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1338:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808248" mac_address="1458d0589ee3">
      <ip address="10.10.1.56" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1338" hardware_type="m510"/>
    <host name="node55.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.32"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1338.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node56" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1324" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808114">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node56:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1324:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808249" mac_address="1458d058af93">
      <ip address="10.10.1.57" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1324" hardware_type="m510"/>
    <host name="node56.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.18"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1324.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node57" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1319" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808056">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node57:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1319:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808250" mac_address="1458d058df43">
      <ip address="10.10.1.58" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1319" hardware_type="m510"/>
    <host name="node57.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.13"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1319.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node58" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1330" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808098">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node58:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1330:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808251" mac_address="1458d058aff3">
      <ip address="10.10.1.59" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1330" hardware_type="m510"/>
    <host name="node58.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.24"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1330.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node59" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0917" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808108">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node59:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0917:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808252" mac_address="1458d0583fd3">
      <ip address="10.10.1.60" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0917" hardware_type="m510"/>
    <host name="node59.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.87"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0917.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node60" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0818" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808111">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node60:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0818:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808253" mac_address="1458d0589f53">
      <ip address="10.10.1.61" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0818" hardware_type="m510"/>
    <host name="node60.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.43"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0818.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node61" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1307" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808062">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node61:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1307:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808254" mac_address="ecb1d7851a53">
      <ip address="10.10.1.62" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1307" hardware_type="m510"/>
    <host name="node61.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.1"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1307.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node62" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0932" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808174">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node62:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0932:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808255" mac_address="1458d058afb3">
      <ip address="10.10.1.63" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0932" hardware_type="m510"/>
    <host name="node62.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.102"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0932.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node63" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0812" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808118">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node63:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0812:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808256" mac_address="1458d0587f83">
      <ip address="10.10.1.64" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0812" hardware_type="m510"/>
    <host name="node63.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.37"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0812.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node64" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0938" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808159">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node64:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0938:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808257" mac_address="1458d0583ea3">
      <ip address="10.10.1.65" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0938" hardware_type="m510"/>
    <host name="node64.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.108"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0938.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node65" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0901" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808049">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node65:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0901:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808258" mac_address="ecb1d7850ac3">
      <ip address="10.10.1.66" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0901" hardware_type="m510"/>
    <host name="node65.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.71"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0901.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node66" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0820" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808100">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node66:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0820:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808259" mac_address="ecb1d7856a83">
      <ip address="10.10.1.67" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0820" hardware_type="m510"/>
    <host name="node66.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.45"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0820.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node67" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0810" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808130">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node67:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0810:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808260" mac_address="1458d058cfd3">
      <ip address="10.10.1.68" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0810" hardware_type="m510"/>
    <host name="node67.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.35"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0810.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node68" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0832" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808050">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node68:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0832:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808261" mac_address="ecb1d7856ae3">
      <ip address="10.10.1.69" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0832" hardware_type="m510"/>
    <host name="node68.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.57"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0832.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node69" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1337" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808132">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node69:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1337:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808262" mac_address="ecb1d7856ad3">
      <ip address="10.10.1.70" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1337" hardware_type="m510"/>
    <host name="node69.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.31"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1337.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node70" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1112" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808150">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node70:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1112:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808263" mac_address="1458d0582ec3">
      <ip address="10.10.1.71" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1112" hardware_type="m510"/>
    <host name="node70.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.172"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1112.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node71" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1344" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808102">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node71:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1344:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808264" mac_address="1458d058bfc3">
      <ip address="10.10.1.72" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1344" hardware_type="m510"/>
    <host name="node71.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.38"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1344.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node72" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1311" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808120">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node72:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1311:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808265" mac_address="ecb1d7857a13">
      <ip address="10.10.1.73" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1311" hardware_type="m510"/>
    <host name="node72.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.5"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1311.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node73" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0919" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808140">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node73:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0919:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808266" mac_address="1458d0583f13">
      <ip address="10.10.1.74" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0919" hardware_type="m510"/>
    <host name="node73.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.89"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0919.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node74" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1131" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808096">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node74:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1131:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808267" mac_address="1458d0581f73">
      <ip address="10.10.1.75" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1131" hardware_type="m510"/>
    <host name="node74.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.191"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1131.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node75" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1322" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808053">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node75:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1322:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808268" mac_address="1458d0582f93">
      <ip address="10.10.1.76" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1322" hardware_type="m510"/>
    <host name="node75.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.16"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1322.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node76" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1304" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808099">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node76:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1304:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808269" mac_address="1458d058fe33">
      <ip address="10.10.1.77" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1304" hardware_type="m510"/>
    <host name="node76.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.254"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1304.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node77" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1132" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808037">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node77:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1132:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808270" mac_address="ecb1d7854a33">
      <ip address="10.10.1.78" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1132" hardware_type="m510"/>
    <host name="node77.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.192"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1132.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node78" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0916" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808126">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node78:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0916:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808271" mac_address="1458d0583f03">
      <ip address="10.10.1.79" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0916" hardware_type="m510"/>
    <host name="node78.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.86"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0916.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node79" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1210" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808071">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node79:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1210:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808272" mac_address="1458d0583f43">
      <ip address="10.10.1.80" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1210" hardware_type="m510"/>
    <host name="node79.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.215"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1210.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node80" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1025" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808051">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node80:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1025:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808273" mac_address="ecb1d7857ab3">
      <ip address="10.10.1.81" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1025" hardware_type="m510"/>
    <host name="node80.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.140"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1025.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node81" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1328" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808063">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node81:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1328:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808274" mac_address="1458d0583fe3">
      <ip address="10.10.1.82" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1328" hardware_type="m510"/>
    <host name="node81.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.22"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1328.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node82" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0941" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808055">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node82:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0941:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808275" mac_address="1458d0580fc3">
      <ip address="10.10.1.83" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0941" hardware_type="m510"/>
    <host name="node82.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.111"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0941.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node83" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1310" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808156">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node83:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1310:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808276" mac_address="1458d058cf83">
      <ip address="10.10.1.84" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1310" hardware_type="m510"/>
    <host name="node83.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.4"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1310.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node84" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0804" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808043">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node84:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0804:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808277" mac_address="ecb1d7856af3">
      <ip address="10.10.1.85" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0804" hardware_type="m510"/>
    <host name="node84.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.29"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0804.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node85" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0831" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808072">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node85:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0831:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808278" mac_address="1458d0589f43">
      <ip address="10.10.1.86" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0831" hardware_type="m510"/>
    <host name="node85.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.56"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0831.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node86" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1017" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808106">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node86:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1017:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808279" mac_address="1458d0585fe3">
      <ip address="10.10.1.87" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1017" hardware_type="m510"/>
    <host name="node86.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.132"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1017.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node87" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0936" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808059">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node87:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0936:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808280" mac_address="1458d0589fa3">
      <ip address="10.10.1.88" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0936" hardware_type="m510"/>
    <host name="node87.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.106"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0936.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node88" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0911" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808038">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node88:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0911:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808281" mac_address="1458d058cf93">
      <ip address="10.10.1.89" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0911" hardware_type="m510"/>
    <host name="node88.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.81"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0911.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node89" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0819" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808081">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node89:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0819:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808282" mac_address="1458d0588fa3">
      <ip address="10.10.1.90" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0819" hardware_type="m510"/>
    <host name="node89.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.44"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0819.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node90" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1244" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808190">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node90:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1244:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808283" mac_address="1458d0581f53">
      <ip address="10.10.1.91" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1244" hardware_type="m510"/>
    <host name="node90.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.249"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1244.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node91" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0943" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808080">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node91:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0943:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808284" mac_address="1458d0589fc3">
      <ip address="10.10.1.92" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0943" hardware_type="m510"/>
    <host name="node91.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.113"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0943.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node92" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1019" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808082">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node92:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1019:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808285" mac_address="ecb1d7852ae3">
      <ip address="10.10.1.93" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1019" hardware_type="m510"/>
    <host name="node92.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.134"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1019.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node93" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1333" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808077">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node93:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1333:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808286" mac_address="ecb1d7851ae3">
      <ip address="10.10.1.94" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1333" hardware_type="m510"/>
    <host name="node93.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.27"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1333.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node94" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1317" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808044">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node94:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1317:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808287" mac_address="1458d0589f03">
      <ip address="10.10.1.95" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1317" hardware_type="m510"/>
    <host name="node94.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.11"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1317.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node95" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1007" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808087">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node95:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1007:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808288" mac_address="1458d0582f63">
      <ip address="10.10.1.96" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1007" hardware_type="m510"/>
    <host name="node95.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.122"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1007.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node96" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1039" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808189">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node96:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1039:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808289" mac_address="ecb1d7855a03">
      <ip address="10.10.1.97" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1039" hardware_type="m510"/>
    <host name="node96.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.154"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1039.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node97" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1043" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808143">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node97:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1043:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808290" mac_address="1458d058eff3">
      <ip address="10.10.1.98" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1043" hardware_type="m510"/>
    <host name="node97.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.158"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1043.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node98" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1320" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808041">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node98:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1320:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808291" mac_address="1458d058cf73">
      <ip address="10.10.1.99" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1320" hardware_type="m510"/>
    <host name="node98.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.14"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1320.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node99" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0921" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808173">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node99:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0921:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808292" mac_address="1458d058ffe3">
      <ip address="10.10.1.100" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0921" hardware_type="m510"/>
    <host name="node99.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.91"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0921.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node100" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0844" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808045">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node100:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0844:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808293" mac_address="1458d058cf03">
      <ip address="10.10.1.101" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0844" hardware_type="m510"/>
    <host name="node100.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.69"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0844.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node101" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1314" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808091">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node101:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1314:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808294" mac_address="1458d058ff93">
      <ip address="10.10.1.102" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1314" hardware_type="m510"/>
    <host name="node101.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.8"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1314.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node102" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0928" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808137">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node102:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0928:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808295" mac_address="ecb1d7854a23">
      <ip address="10.10.1.103" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0928" hardware_type="m510"/>
    <host name="node102.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.98"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0928.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node103" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0903" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808075">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node103:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0903:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808296" mac_address="1458d058ff23">
      <ip address="10.10.1.104" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0903" hardware_type="m510"/>
    <host name="node103.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.73"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0903.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node104" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1302" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808170">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node104:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1302:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808297" mac_address="1458d0584f23">
      <ip address="10.10.1.105" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1302" hardware_type="m510"/>
    <host name="node104.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.252"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1302.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node105" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1219" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808136">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node105:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1219:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808298" mac_address="1458d0587fd3">
      <ip address="10.10.1.106" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1219" hardware_type="m510"/>
    <host name="node105.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.224"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1219.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node106" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0822" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808074">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node106:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0822:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808299" mac_address="ecb1d7856a93">
      <ip address="10.10.1.107" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0822" hardware_type="m510"/>
    <host name="node106.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.47"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0822.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node107" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0945" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808057">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node107:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0945:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808300" mac_address="ecb1d7855ad3">
      <ip address="10.10.1.108" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0945" hardware_type="m510"/>
    <host name="node107.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.115"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0945.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node108" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1134" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808131">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node108:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1134:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808301" mac_address="ecb1d7851aa3">
      <ip address="10.10.1.109" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1134" hardware_type="m510"/>
    <host name="node108.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.194"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1134.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node109" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0841" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808163">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node109:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0841:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808302" mac_address="ecb1d7853aa3">
      <ip address="10.10.1.110" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0841" hardware_type="m510"/>
    <host name="node109.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.66"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0841.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node110" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1339" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808123">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node110:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1339:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808303" mac_address="1458d0589f93">
      <ip address="10.10.1.111" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1339" hardware_type="m510"/>
    <host name="node110.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.33"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1339.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node111" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0836" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808164">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node111:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0836:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808304" mac_address="ecb1d7854a73">
      <ip address="10.10.1.112" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0836" hardware_type="m510"/>
    <host name="node111.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.61"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0836.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node112" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0838" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808065">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node112:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0838:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808305" mac_address="1458d0585fc3">
      <ip address="10.10.1.113" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0838" hardware_type="m510"/>
    <host name="node112.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.63"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0838.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node113" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1236" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808060">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node113:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1236:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808306" mac_address="1458d0582c63">
      <ip address="10.10.1.114" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1236" hardware_type="m510"/>
    <host name="node113.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.241"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1236.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node114" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1334" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808181">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node114:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1334:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808307" mac_address="ecb1d7855a13">
      <ip address="10.10.1.115" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1334" hardware_type="m510"/>
    <host name="node114.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.28"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1334.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node115" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1235" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808129">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node115:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1235:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808308" mac_address="ecb1d7855ac3">
      <ip address="10.10.1.116" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1235" hardware_type="m510"/>
    <host name="node115.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.240"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1235.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node116" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1105" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808182">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node116:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1105:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808309" mac_address="ecb1d7850a43">
      <ip address="10.10.1.117" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1105" hardware_type="m510"/>
    <host name="node116.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.165"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1105.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node117" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1343" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808161">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node117:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1343:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808310" mac_address="1458d058ef03">
      <ip address="10.10.1.118" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1343" hardware_type="m510"/>
    <host name="node117.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.37"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1343.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node118" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1222" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808127">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node118:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1222:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808311" mac_address="ecb1d7852ad3">
      <ip address="10.10.1.119" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1222" hardware_type="m510"/>
    <host name="node118.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.227"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1222.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node119" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1216" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808107">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node119:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1216:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808312" mac_address="ecb1d7850a53">
      <ip address="10.10.1.120" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1216" hardware_type="m510"/>
    <host name="node119.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.221"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1216.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node120" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1143" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808122">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node120:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1143:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808313" mac_address="1458d0582f83">
      <ip address="10.10.1.121" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1143" hardware_type="m510"/>
    <host name="node120.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.203"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1143.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node121" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0908" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808088">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node121:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0908:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808314" mac_address="1458d058af83">
      <ip address="10.10.1.122" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0908" hardware_type="m510"/>
    <host name="node121.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.78"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0908.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node122" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1122" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808095">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node122:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1122:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808315" mac_address="1458d0581fe3">
      <ip address="10.10.1.123" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1122" hardware_type="m510"/>
    <host name="node122.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.182"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1122.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node123" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1133" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808039">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node123:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1133:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808316" mac_address="1458d0582f13">
      <ip address="10.10.1.124" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1133" hardware_type="m510"/>
    <host name="node123.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.193"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1133.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node124" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1029" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808124">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node124:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1029:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808317" mac_address="1458d058ff03">
      <ip address="10.10.1.125" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1029" hardware_type="m510"/>
    <host name="node124.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.144"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1029.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node125" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1018" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808109">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node125:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1018:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808318" mac_address="1458d0587f23">
      <ip address="10.10.1.126" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1018" hardware_type="m510"/>
    <host name="node125.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.133"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1018.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node126" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1013" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808115">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node126:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1013:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808319" mac_address="1458d0584f43">
      <ip address="10.10.1.127" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1013" hardware_type="m510"/>
    <host name="node126.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.128"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1013.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node127" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0934" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808101">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node127:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0934:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808320" mac_address="1458d0584f93">
      <ip address="10.10.1.128" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0934" hardware_type="m510"/>
    <host name="node127.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.104"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0934.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node128" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0843" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808139">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node128:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0843:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808321" mac_address="1458d0588f93">
      <ip address="10.10.1.129" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0843" hardware_type="m510"/>
    <host name="node128.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.68"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0843.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node129" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0939" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808032">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node129:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0939:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808322" mac_address="1458d0586f03">
      <ip address="10.10.1.130" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0939" hardware_type="m510"/>
    <host name="node129.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.109"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0939.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node130" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1345" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808142">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node130:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1345:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808323" mac_address="1458d058ffa3">
      <ip address="10.10.1.131" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1345" hardware_type="m510"/>
    <host name="node130.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.39"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1345.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node131" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1107" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808103">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node131:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1107:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808324" mac_address="1458d058efc3">
      <ip address="10.10.1.132" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1107" hardware_type="m510"/>
    <host name="node131.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.167"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1107.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node132" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0925" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808168">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node132:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0925:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808325" mac_address="ecb1d7853a13">
      <ip address="10.10.1.133" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0925" hardware_type="m510"/>
    <host name="node132.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.95"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0925.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node133" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1315" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808117">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node133:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1315:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808326" mac_address="1458d0581fb3">
      <ip address="10.10.1.134" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1315" hardware_type="m510"/>
    <host name="node133.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.9"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1315.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node134" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1144" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808061">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node134:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1144:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808327" mac_address="1458d0587ff3">
      <ip address="10.10.1.135" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1144" hardware_type="m510"/>
    <host name="node134.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.204"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1144.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node135" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1120" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808090">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node135:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1120:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808328" mac_address="1458d058af13">
      <ip address="10.10.1.136" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1120" hardware_type="m510"/>
    <host name="node135.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.180"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1120.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node136" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1028" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808085">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node136:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1028:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808329" mac_address="1458d058bf43">
      <ip address="10.10.1.137" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1028" hardware_type="m510"/>
    <host name="node136.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.143"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1028.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node137" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0926" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808084">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node137:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0926:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808330" mac_address="1458d058eec3">
      <ip address="10.10.1.138" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0926" hardware_type="m510"/>
    <host name="node137.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.96"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0926.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node138" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1329" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808187">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node138:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1329:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808331" mac_address="ecb1d7855a33">
      <ip address="10.10.1.139" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1329" hardware_type="m510"/>
    <host name="node138.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.23"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1329.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node139" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1024" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808178">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node139:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1024:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808332" mac_address="ecb1d7855ae3">
      <ip address="10.10.1.140" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1024" hardware_type="m510"/>
    <host name="node139.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.139"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1024.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node140" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1313" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808185">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node140:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1313:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808333" mac_address="1458d058af33">
      <ip address="10.10.1.141" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1313" hardware_type="m510"/>
    <host name="node140.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.7"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1313.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node141" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1040" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808110">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node141:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1040:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808334" mac_address="1458d058fe23">
      <ip address="10.10.1.142" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1040" hardware_type="m510"/>
    <host name="node141.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.155"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1040.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node142" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1125" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808036">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node142:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1125:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808335" mac_address="ecb1d7850a93">
      <ip address="10.10.1.143" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1125" hardware_type="m510"/>
    <host name="node142.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.185"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1125.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node143" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1332" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808078">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node143:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1332:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808336" mac_address="1458d0582f23">
      <ip address="10.10.1.144" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1332" hardware_type="m510"/>
    <host name="node143.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.26"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1332.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node144" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms0910" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808089">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node144:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0910:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808337" mac_address="1458d0583ff3">
      <ip address="10.10.1.145" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms0910" hardware_type="m510"/>
    <host name="node144.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.80"/>
    <services>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms0910.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node145" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1126" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808125">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node145:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1126:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808338" mac_address="1458d058dfb3">
      <ip address="10.10.1.146" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1126" hardware_type="m510"/>
    <host name="node145.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.186"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1126.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node146" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1044" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808046">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node146:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1044:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808339" mac_address="1458d058df53">
      <ip address="10.10.1.147" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1044" hardware_type="m510"/>
    <host name="node146.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.159"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1044.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node147" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1340" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808176">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node147:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1340:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808340" mac_address="ecb1d7854a53">
      <ip address="10.10.1.148" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1340" hardware_type="m510"/>
    <host name="node147.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.34"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1340.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node148" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1137" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808175">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node148:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1137:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808341" mac_address="1458d0584fc3">
      <ip address="10.10.1.149" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1137" hardware_type="m510"/>
    <host name="node148.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.197"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1137.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node149" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1321" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808076">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node149:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1321:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808342" mac_address="1458d058dfc3">
      <ip address="10.10.1.150" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1321" hardware_type="m510"/>
    <host name="node149.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.15"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1321.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node150" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1241" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808064">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node150:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1241:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808343" mac_address="1458d0582fe3">
      <ip address="10.10.1.151" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1241" hardware_type="m510"/>
    <host name="node150.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.246"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1241.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node151" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1101" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808184">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node151:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1101:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808344" mac_address="1458d058ef33">
      <ip address="10.10.1.152" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1101" hardware_type="m510"/>
    <host name="node151.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.161"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1101.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node152" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1135" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808094">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node152:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1135:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808345" mac_address="1458d0588fb3">
      <ip address="10.10.1.153" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1135" hardware_type="m510"/>
    <host name="node152.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.195"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1135.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node153" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1318" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808177">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node153:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1318:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808346" mac_address="1458d0580f13">
      <ip address="10.10.1.154" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1318" hardware_type="m510"/>
    <host name="node153.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.12"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1318.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node154" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1145" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808188">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node154:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1145:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808347" mac_address="ecb1d7855a93">
      <ip address="10.10.1.155" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1145" hardware_type="m510"/>
    <host name="node154.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.205"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1145.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node155" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1130" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808066">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node155:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1130:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808348" mac_address="1458d0584e83">
      <ip address="10.10.1.156" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1130" hardware_type="m510"/>
    <host name="node155.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.190"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1130.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node156" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1012" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808116">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node156:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1012:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808349" mac_address="ecb1d7853a83">
      <ip address="10.10.1.157" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1012" hardware_type="m510"/>
    <host name="node156.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.127"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1012.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node157" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1118" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808135">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node157:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1118:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808350" mac_address="ecb1d7852a23">
      <ip address="10.10.1.158" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1118" hardware_type="m510"/>
    <host name="node157.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.178"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1118.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node158" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1316" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808033">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node158:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1316:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808351" mac_address="ecb1d7852a63">
      <ip address="10.10.1.159" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1316" hardware_type="m510"/>
    <host name="node158.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.218.10"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1316.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node159" exclusive="true" component_manager_id="urn:publicid:IDN+utah.cloudlab.us+authority+cm" component_id="urn:publicid:IDN+utah.cloudlab.us+node+ms1301" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808149">
    <sliver_type name="raw-pc"/>
    <hardware_type name="m510"/>
    <interface client_id="node159:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1301:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808352" mac_address="1458d0586f43">
      <ip address="10.10.1.160" type="ipv4" netmask="255.255.255.0"/>
    </interface>
    <emulab:vnode name="ms1301" hardware_type="m510"/>
    <host name="node159.cluster-miner.cloudprof-PG0.utah.cloudlab.us" ipv4="128.110.217.251"/>
    <services>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="probirr"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="whitspen"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="arjunsh"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="ssmtariq"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="akazad"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="lmenard"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="wilkowsk"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="SonjoyKP"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="sonjoyp"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="eejoylim"/>
      <login authentication="ssh-keys" hostname="ms1301.utah.cloudlab.us" port="22" username="Shreyba"/>
      <emulab:console server="boss.utah.cloudlab.us"/>
      <emulab:recovery available="true"/>
      <emulab:powercycle available="true"/>
      <emulab:imageable available="true"/>
    </services>
  </node>
  <link xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="link-1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808192" vlantag="293">
    <interface_ref client_id="node0:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1041:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808193"/>
    <interface_ref client_id="node1:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1325:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808194"/>
    <interface_ref client_id="node2:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1108:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808195"/>
    <interface_ref client_id="node3:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0933:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808196"/>
    <interface_ref client_id="node4:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0931:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808197"/>
    <interface_ref client_id="node5:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1308:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808198"/>
    <interface_ref client_id="node6:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0907:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808199"/>
    <interface_ref client_id="node7:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0904:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808200"/>
    <interface_ref client_id="node8:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0837:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808201"/>
    <interface_ref client_id="node9:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1303:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808202"/>
    <interface_ref client_id="node10:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0909:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808203"/>
    <interface_ref client_id="node11:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1342:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808204"/>
    <interface_ref client_id="node12:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1305:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808205"/>
    <interface_ref client_id="node13:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0823:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808206"/>
    <interface_ref client_id="node14:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0813:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808207"/>
    <interface_ref client_id="node15:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1327:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808208"/>
    <interface_ref client_id="node16:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1232:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808209"/>
    <interface_ref client_id="node17:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0915:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808210"/>
    <interface_ref client_id="node18:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1033:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808211"/>
    <interface_ref client_id="node19:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1341:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808212"/>
    <interface_ref client_id="node20:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1331:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808213"/>
    <interface_ref client_id="node21:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1209:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808214"/>
    <interface_ref client_id="node22:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1002:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808215"/>
    <interface_ref client_id="node23:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1233:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808216"/>
    <interface_ref client_id="node24:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1336:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808217"/>
    <interface_ref client_id="node25:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0826:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808218"/>
    <interface_ref client_id="node26:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1214:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808219"/>
    <interface_ref client_id="node27:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0923:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808220"/>
    <interface_ref client_id="node28:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1031:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808221"/>
    <interface_ref client_id="node29:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0918:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808222"/>
    <interface_ref client_id="node30:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0935:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808223"/>
    <interface_ref client_id="node31:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1004:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808224"/>
    <interface_ref client_id="node32:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1022:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808225"/>
    <interface_ref client_id="node33:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1227:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808226"/>
    <interface_ref client_id="node34:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0930:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808227"/>
    <interface_ref client_id="node35:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0802:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808228"/>
    <interface_ref client_id="node36:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0827:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808229"/>
    <interface_ref client_id="node37:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1306:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808230"/>
    <interface_ref client_id="node38:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1114:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808231"/>
    <interface_ref client_id="node39:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1326:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808232"/>
    <interface_ref client_id="node40:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1335:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808233"/>
    <interface_ref client_id="node41:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1312:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808234"/>
    <interface_ref client_id="node42:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1119:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808235"/>
    <interface_ref client_id="node43:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1224:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808236"/>
    <interface_ref client_id="node44:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1003:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808237"/>
    <interface_ref client_id="node45:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1309:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808238"/>
    <interface_ref client_id="node46:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1240:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808239"/>
    <interface_ref client_id="node47:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1223:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808240"/>
    <interface_ref client_id="node48:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1230:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808241"/>
    <interface_ref client_id="node49:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1208:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808242"/>
    <interface_ref client_id="node50:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0801:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808243"/>
    <interface_ref client_id="node51:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1323:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808244"/>
    <interface_ref client_id="node52:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0940:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808245"/>
    <interface_ref client_id="node53:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0913:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808246"/>
    <interface_ref client_id="node54:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1205:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808247"/>
    <interface_ref client_id="node55:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1338:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808248"/>
    <interface_ref client_id="node56:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1324:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808249"/>
    <interface_ref client_id="node57:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1319:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808250"/>
    <interface_ref client_id="node58:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1330:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808251"/>
    <interface_ref client_id="node59:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0917:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808252"/>
    <interface_ref client_id="node60:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0818:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808253"/>
    <interface_ref client_id="node61:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1307:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808254"/>
    <interface_ref client_id="node62:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0932:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808255"/>
    <interface_ref client_id="node63:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0812:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808256"/>
    <interface_ref client_id="node64:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0938:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808257"/>
    <interface_ref client_id="node65:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0901:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808258"/>
    <interface_ref client_id="node66:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0820:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808259"/>
    <interface_ref client_id="node67:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0810:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808260"/>
    <interface_ref client_id="node68:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0832:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808261"/>
    <interface_ref client_id="node69:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1337:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808262"/>
    <interface_ref client_id="node70:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1112:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808263"/>
    <interface_ref client_id="node71:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1344:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808264"/>
    <interface_ref client_id="node72:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1311:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808265"/>
    <interface_ref client_id="node73:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0919:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808266"/>
    <interface_ref client_id="node74:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1131:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808267"/>
    <interface_ref client_id="node75:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1322:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808268"/>
    <interface_ref client_id="node76:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1304:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808269"/>
    <interface_ref client_id="node77:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1132:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808270"/>
    <interface_ref client_id="node78:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0916:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808271"/>
    <interface_ref client_id="node79:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1210:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808272"/>
    <interface_ref client_id="node80:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1025:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808273"/>
    <interface_ref client_id="node81:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1328:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808274"/>
    <interface_ref client_id="node82:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0941:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808275"/>
    <interface_ref client_id="node83:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1310:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808276"/>
    <interface_ref client_id="node84:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0804:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808277"/>
    <interface_ref client_id="node85:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0831:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808278"/>
    <interface_ref client_id="node86:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1017:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808279"/>
    <interface_ref client_id="node87:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0936:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808280"/>
    <interface_ref client_id="node88:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0911:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808281"/>
    <interface_ref client_id="node89:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0819:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808282"/>
    <interface_ref client_id="node90:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1244:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808283"/>
    <interface_ref client_id="node91:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0943:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808284"/>
    <interface_ref client_id="node92:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1019:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808285"/>
    <interface_ref client_id="node93:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1333:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808286"/>
    <interface_ref client_id="node94:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1317:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808287"/>
    <interface_ref client_id="node95:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1007:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808288"/>
    <interface_ref client_id="node96:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1039:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808289"/>
    <interface_ref client_id="node97:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1043:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808290"/>
    <interface_ref client_id="node98:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1320:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808291"/>
    <interface_ref client_id="node99:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0921:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808292"/>
    <interface_ref client_id="node100:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0844:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808293"/>
    <interface_ref client_id="node101:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1314:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808294"/>
    <interface_ref client_id="node102:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0928:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808295"/>
    <interface_ref client_id="node103:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0903:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808296"/>
    <interface_ref client_id="node104:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1302:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808297"/>
    <interface_ref client_id="node105:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1219:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808298"/>
    <interface_ref client_id="node106:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0822:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808299"/>
    <interface_ref client_id="node107:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0945:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808300"/>
    <interface_ref client_id="node108:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1134:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808301"/>
    <interface_ref client_id="node109:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0841:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808302"/>
    <interface_ref client_id="node110:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1339:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808303"/>
    <interface_ref client_id="node111:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0836:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808304"/>
    <interface_ref client_id="node112:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0838:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808305"/>
    <interface_ref client_id="node113:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1236:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808306"/>
    <interface_ref client_id="node114:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1334:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808307"/>
    <interface_ref client_id="node115:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1235:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808308"/>
    <interface_ref client_id="node116:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1105:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808309"/>
    <interface_ref client_id="node117:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1343:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808310"/>
    <interface_ref client_id="node118:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1222:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808311"/>
    <interface_ref client_id="node119:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1216:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808312"/>
    <interface_ref client_id="node120:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1143:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808313"/>
    <interface_ref client_id="node121:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0908:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808314"/>
    <interface_ref client_id="node122:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1122:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808315"/>
    <interface_ref client_id="node123:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1133:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808316"/>
    <interface_ref client_id="node124:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1029:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808317"/>
    <interface_ref client_id="node125:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1018:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808318"/>
    <interface_ref client_id="node126:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1013:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808319"/>
    <interface_ref client_id="node127:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0934:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808320"/>
    <interface_ref client_id="node128:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0843:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808321"/>
    <interface_ref client_id="node129:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0939:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808322"/>
    <interface_ref client_id="node130:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1345:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808323"/>
    <interface_ref client_id="node131:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1107:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808324"/>
    <interface_ref client_id="node132:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0925:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808325"/>
    <interface_ref client_id="node133:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1315:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808326"/>
    <interface_ref client_id="node134:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1144:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808327"/>
    <interface_ref client_id="node135:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1120:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808328"/>
    <interface_ref client_id="node136:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1028:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808329"/>
    <interface_ref client_id="node137:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0926:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808330"/>
    <interface_ref client_id="node138:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1329:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808331"/>
    <interface_ref client_id="node139:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1024:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808332"/>
    <interface_ref client_id="node140:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1313:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808333"/>
    <interface_ref client_id="node141:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1040:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808334"/>
    <interface_ref client_id="node142:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1125:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808335"/>
    <interface_ref client_id="node143:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1332:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808336"/>
    <interface_ref client_id="node144:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms0910:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808337"/>
    <interface_ref client_id="node145:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1126:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808338"/>
    <interface_ref client_id="node146:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1044:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808339"/>
    <interface_ref client_id="node147:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1340:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808340"/>
    <interface_ref client_id="node148:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1137:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808341"/>
    <interface_ref client_id="node149:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1321:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808342"/>
    <interface_ref client_id="node150:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1241:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808343"/>
    <interface_ref client_id="node151:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1101:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808344"/>
    <interface_ref client_id="node152:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1135:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808345"/>
    <interface_ref client_id="node153:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1318:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808346"/>
    <interface_ref client_id="node154:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1145:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808347"/>
    <interface_ref client_id="node155:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1130:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808348"/>
    <interface_ref client_id="node156:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1012:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808349"/>
    <interface_ref client_id="node157:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1118:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808350"/>
    <interface_ref client_id="node158:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1316:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808351"/>
    <interface_ref client_id="node159:eth1" component_id="urn:publicid:IDN+utah.cloudlab.us+interface+ms1301:eth1" sliver_id="urn:publicid:IDN+utah.cloudlab.us+sliver+1808352"/>
    <link_type name="lan"/>
    <emulab:best_effort enabled="true"/>
    <component_manager name="urn:publicid:IDN+utah.cloudlab.us+authority+cm"/>
    <emulab:switchpath>ms-chassis13-switchb:bighp1 ms-chassis11-switchb:bighp1 ms-chassis8-switchb:bighp1 ms-chassis9-switchb:bighp1 ms-chassis12-switchb:bighp1 ms-chassis10-switchb:bighp1</emulab:switchpath>
  </link>
  <rspec_tour xmlns="http://www.protogeni.net/resources/rspec/ext/apt-tour/1">
    <description type="markdown">Variable number of nodes in a lan. You have the option of picking from one
of several standard images we provide, or just use the default (typically a recent
version of Ubuntu). You may also optionally pick the specific hardware type for
all the nodes in the lan. </description>
    <instructions type="markdown">Wait for the experiment to start, and then log into one or more of the nodes
by clicking on them in the toplogy, and choosing the `shell` menu option.
Use `sudo` to run root commands. 
</instructions>
  </rspec_tour>
  <data_set xmlns="http://www.protogeni.net/resources/rspec/ext/profile-parameters/1">
    <data_item name="emulab.net.parameter.linkSpeed">10000000</data_item>
    <data_item name="emulab.net.parameter.tempFileSystemSize">0</data_item>
    <data_item name="emulab.net.parameter.useVMs">False</data_item>
    <data_item name="emulab.net.parameter.tempFileSystemMax">False</data_item>
    <data_item name="emulab.net.parameter.tempFileSystemMount">/mydata</data_item>
    <data_item name="emulab.net.parameter.bestEffort">True</data_item>
    <data_item name="emulab.net.parameter.phystype">m510</data_item>
    <data_item name="emulab.net.parameter.sameSwitch">False</data_item>
    <data_item name="emulab.net.parameter.osImage">default</data_item>
    <data_item name="emulab.net.parameter.nodeCount">160</data_item>
    <data_item name="emulab.net.parameter.startVNC">False</data_item>
  </data_set>
  <emulab:portal name="cloudlab" url="https://www.cloudlab.us/status.php?uuid=ba7cd01f-1f6f-11ef-9f39-e4434b2381fc" project="CloudProf" experiment="cluster-miner" sequence="1717175026"/>
  <rs:site_info xmlns:rs="http://www.protogeni.net/resources/rspec/ext/site-info/1">
    <rs:location country="US" latitude="40.750714" longitude="-111.893288"/>
  </rs:site_info>
</rspec>
'''

# Extract host information
host_info = extract_host_info(xml_content)

# Write the extracted information to a file
with open("host_info.txt", "w") as file:
    for entry in host_info:
        file.write(entry + "\n")

print("Host information extracted and saved to host_info.txt")