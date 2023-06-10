{% extends 'base.html' %}
{% load static %}

{% block style %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block ul %}
    <li class="nav-item">
        <a class="nav-link " href="index.html">
        <i class="fa fa-line-chart" style="font-size: 23px;"> </i>


        <span class="menu-title" style="padding:5px;">Dashboard</span>
        </a>
    </li>
    <li class="nav-item active">
        <a class="nav-link " href="index.html">
        <i class="" style="font-size: 23px;"> </i>


        <span class="menu-title" style="padding:5px;">Customer</span>
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="detection.html" >
        <i class="fa fa-bullseye" style="font-size: 25px;"> </i>
        <span class="menu-title" style="padding:5px;">Detection</span>  
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="investigate.html" >
        <i class="fa fa-search" style="font-size: 25px;"></i>
        <span class="menu-title" style="padding:5px;">Investigate</span> 
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="threat_intl.html" >
        
        <i class="fa fa-brain-circuit"></i>
        <span class="menu-title">Threat Intelligence</span> 
        </a>
    </li>

    
    <li class="nav-item">
        <a class="nav-link" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false" aria-controls="ui-basic">
        <i class="menu-icon mdi mdi-file-tree"></i>
        <span class="menu-title">Automation & <br>Orchestration</span>
        <i class="menu-arrow"></i> 
        </a>
        <div class="collapse" id="ui-basic">
        <ul class="nav flex-column sub-menu">
            <li class="nav-item"> <a class="nav-link" href="#choice1">Choice 1</a></li>
            <li class="nav-item"> <a class="nav-link" href="#choice2">Choice 2</a></li>
{% endblock %}

{% block body %}
<div class="content-wrapper">
    <!-- ########################### main card ################################# -->
    <div class="card" style="color: #fff;background-color:#212422b7;">
      <div class="card-title" id="card-title" style="color: #0875f1;padding:20px;border:1px solid gray">
        Add Client Details
      </div>
        <div class="card-body">
          <form action="{% url 'add_client' %}" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <!-- ####################################### organization ##################################### -->
            <div class="row" style="border:1px solid rgb(101, 98, 98);padding:20px;border-radius:10px;">

              <h5 class="heading">Organization</h5>
              <hr>

              <div class="col ">
                <label for="org_id" class="org_label">Organization ID(Umbrella)</label>
                <input type="text" class="form-control " placeholder="organization Id" name="org_id" id="org_id">
              </div>
              <div class="col ">
                <label for="jira_id" class="org_label">Jira ID</label>
                <input type="text" class="form-control " placeholder="jira Id" name="jira_id" id="jira_id">
              </div>
              <div class="col ">
                <label for="org_name" class="org_label">Organization Name</label>
                <input type="text" class="form-control " placeholder="Organization name" name="org_name">
              </div>
              <div class="col ">
                <label for="timezone" class="org_label">Timezone</label>
                <!-- <input type="text" class="form-control " placeholder="timezone" name="timez"> -->
                <select id="timez" class="form-control" name="timez">
                  <option selected>Choose...</option>
                  <option value="Eastern Time">Eastern Time</option>
                  <option value="Eastern Standard Time">Eastern Standard Time</option> 
                  <option value=" Eastern Daylight Time"> Eastern Daylight Time</option> 
                  <option value="Central Time">Central Time</option> 
                  <option value="Central Standard Time">Central Standard Time</option> 
                  <option value="Central Daylight Time">Central Daylight Time</option> 
                  <option value=" Mountain Time"> Mountain Time</option> 
                  <option value="Mountain Standard Time">Mountain Standard Time</option> 
                  <option value="Mountain Daylight Time">Mountain Daylight Time</option> 
                  <option value="Pacific Time">Pacific Time</option> 
                  <option value=" Pacific Standard Time"> Pacific Standard Time</option> 
                  <option value=" Pacific Daylight Time"> Pacific Daylight Time</option> 
                  <option value="Alaska Time">Alaska Time</option> 
                  <option value=" Alaska Standard Time">  Alaska Standard Time</option> 
                  <option value="Alaska Daylight Time">Alaska Daylight Time</option> 
                  <option value="Hawaii Time">Hawaii Time</option> 
                  <option value=" Hawaii Standard Time">  Hawaii Standard Time</option> 
                  <option value=" Hawaii Daylight Time">  Hawaii Daylight Time</option> 
                  
                </select>
              </div>

            </div>
            <!-- ############################## end of organization ########################################### -->

            <!-- ################################### Controls ######################################################## -->
            <div class="control-services" style="padding-top: 20px;">
              <div class="row" style="border:1px solid rgb(101, 98, 98);padding:20px;border-radius:10px">
                <h5 class="heading">Controls</h5>
                <hr>
                <div class="col-md-6">
                  <div class="wraper">
                    <div class="collapsed-menu  bg-0">
                      <a class="collapsed-menu-btn styled-link" >
                        <div><span class="material-symbols-rounded small regular-color ">expand_more</span></div>
                        <p class="regular-color ">Select Controls</p>
                      </a>
                      
                      <div class="services" style="padding-left:20px;margin-top:20px;">
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Securex 
                          </div>
                          <div class="col-md-2">
                            <input type="checkbox" name="securex" id="securex" value="scheckbox" />

                          </div>
                          <div class="col-md-4">
                            Secure Endpoint
                          </div>
                          <div class="col">
                            <input type="checkbox" name="secure_endpoint" id="secure_endpoint" value="scheckbox" />

                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Umbrella
                          </div>
                          <div class="col">
                            <input type="checkbox" name="umbrella" id="umbrella" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Umbrella Investigate
                          </div>
                          <div class="col">
                            <input type="checkbox" name="umbrella_invest" id="umbrella_invest" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Meraki MX 
                          </div>
                          <div class="col">
                            <input type="checkbox" name="meraki_mx" id="meraki_mx" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Meraki SM
                          </div>
                          <div class="col">
                            <input type="checkbox" name="meraki_sm" id="meraki_sm" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Orbital 
                          </div>
                          <div class="col">
                            <input type="checkbox" name="orbital" id="orbital" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Duo
                          </div>
                          <div class="col">
                            <input type="checkbox" name="duo" id="duo" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            CES  
                          </div> 
                          <div class="col">
                            <input type="checkbox" name="ces" id="ces" value="scheckbox" />
                          </div>
                          
                          <div class="col-md-4" >
                            Firewall(ASA)
                          </div>
                          <div class="col">
                            <input type="checkbox" name="firewall" id="firewall" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Secure Malware Analytics
                          </div>
                          <div class="col">
                            <input type="checkbox" name="secure_malware" id="secure_malware" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Stealthwatch Cloud
                          </div>
                          <div class="col">
                            <input type="checkbox" name="stealthwatch" id="stealthwatch" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col">
                            Elastic
                          </div>
                          <div class="col">
                            <input type="checkbox" name="elastic" id="elastic" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Onelogin
                          </div>
                          <div class="col">
                            <input type="checkbox" name="onelogin" id="onelogin" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Azure AD
                          </div>
                          <div class="col">
                            <input type="checkbox" name="azure_ad" id="azure_ad" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            o365
                          </div>
                          <div class="col">
                            <input type="checkbox" name="o365" id="o365" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            SentinelOne
                          </div>
                          <div class="col">
                            <input type="checkbox" name="sentinelOne" id="sentinelOne" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            Cybereason
                          </div>
                          <div class="col">
                            <input type="checkbox" name="cybereason" id="cybereason" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Proofpoint
                          </div>
                          <div class="col">
                            <input type="checkbox" name="proofpoint" id="proofpoint" value="scheckbox" />
                          </div>
                          <div class="col-md-4">
                            PaloAlto
                          </div>
                          <div class="col">
                            <input type="checkbox" name="paloAlto" id="paloAlto" value="scheckbox" />
                          </div>
                        </div>
                        <hr>
                        <div class="row">
                          <div class="col-md-4">
                            Ninja Pro
                          </div>
                          <div class="col">
                            <input type="checkbox" name="ninja_pro" id="ninja_pro" value="scheckbox" />
                          </div>
                          <div class="col">
                          
                          </div>
                          <div class="col">
                            
                          </div>
                        </div>
                        <div></div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  
                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="secure_sh container-secure"  style="border: 1px solid gray;">
                          <div class="label-check">
                            <h5 class="secure_sh" style="padding:10px;" >Securex</h5>
                            <hr>
                          <label for="" class="secure_sh" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="secure_sh" name="securex_subs" id="secure_x" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="secure_sh" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class=" secure_sh" name="securex_managed" id="secure_x" value="managed" />
                          
                          </div>
                          <div class="input-field">
                          <!-- <input class="form-control secure_sh" name="securex" id="securex" type="text" value="securex" size="50" hidden /><br> -->
                          <input class="form-control secure_sh" name="securex_client_id"  type="text" placeholder="Client Id" size="50"/><br>
                          <input class="form-control secure_sh" name="securex_secret"  type="text" placeholder="Secret key" size="40"/><br>
                          <input class="form-control secure_sh" name="securex_region"  type="text" placeholder="Region" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- **--------------------------------- secure endpoint ------------------------------** -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="secure_pnt container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="secure_pnt" style="padding:10px;" >Secure Endpoint</h5>
                            <hr>
                          <label for="" class="secure_pnt" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="secure_pnt" name="secure_endpnt_subs" id="secure_endpnt_subs" value="subscribed"/>
                          &nbsp  &nbsp &nbsp
                          <label for="" class="secure_pnt" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class=" secure_pnt" name="secure_endpnt_managed" id="secure_endpnt_managed" value="managed"/>
                          
                          </div>
                          <div class="input-field">
                          <!-- <input class="form-control secure_pnt" name="secure_endpnt"  type="text" value="secure endpoint" size="50" hidden/><br> -->
                          <input class="form-control secure_pnt" name="secure_endpnt_cid"  type="text" placeholder="Client Id" size="50"/><br>
                          <input class="form-control secure_pnt" name="secure_endpnt_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control secure_pnt" name="secure_endpnt_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>

                <!-- **------------------------------- umbrella -------------------------------** -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="umb container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="umb" style="padding:10px;" >Umbrella</h5>
                            <hr>
                          <label for="" class="umb" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="umb" name="umb_subs" id="umb_subs" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="umb" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class=" umb" name="umb_managed" id="umb_subs" value="managed"/>
                          
                          </div>
                          <div class="input-field">
                            <p>Reporting</p>
                            <input class="form-control umb" name="umbreport_secret"  type="text" placeholder="Api key" size="40"/><br>
                            <input class="form-control umb" name="umbreport_region"  type="text" placeholder="Secret" size="40"/><br>
                          </div>
                          <div class="input-field">
                            <p>Network Device</p>
                            <input class="form-control umb" name="umbntwrk_secret"  type="text" placeholder="Api key" size="40"/><br>
                            <input class="form-control umb" name="umbntwrk_region"  type="text" placeholder="Secret" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- **------------------------------- Umbrella investigate -----------------------------** -->
                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="umb_invest container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="umb_invest" style="padding:10px;" >Umbrella Investigate</h5>
                            <hr>
                          <label for="" class="umb_invest" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="umb_invest" name="umb_invest_subs" id="umb_invest_subs" value="subscribed"/>
                          &nbsp  &nbsp &nbsp
                          <label for="" class="umb_invest" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class=" umb_invest" name="umb_invest_manage" id="umb_invest_manage" value="managed"/>
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control umb_invest" name="umbinv_secret"  type="text" placeholder="Umbrella Network Devices" size="40"/><br>
                          <input class="form-control umb_invest" name="umbinv_region"  type="text" placeholder="Legacy Network Devices" size="40"/><br>
                          <input class="form-control umb_invest" name="umbinv_region"  type="text" placeholder="Umbrella Reporting" size="40"/><br>
                          <input class="form-control umb_invest" name="umbinv_region"  type="text" placeholder="Umbrella Management" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- --------------------------------------- meraki_mx----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="merakimx container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="merakimx" style="padding:10px;" >Meraki Mx </h5>
                            <hr>
                          <label for="" class="meraki_mx" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="merakimx" name="mx_sub" id="meraki_mx" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="meraki_mx" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="meraki_mx" name="mx_managed" id="meraki_mx" value="managed" />
                          
                          </div>
                          <div class="input-field">
                        
                          <input class="form-control meraki_mx" name="mx_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control meraki_mx" name="mx_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end meraki_mx--------------------------- -->
                  <!-- --------------------------------------- meraki_sm----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="merakism container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="merakism" style="padding:10px;" >Meraki Sm </h5>
                            <hr>
                          <label for="" class="merakism" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="merakism" name="sm_sub" id="meraki_sm" value="subscribed"/>
                          &nbsp  &nbsp &nbsp
                          <label for="" class="merakism" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="merakism" name="sm_managed" id="meraki_sm" value="managed"/>
                          
                          </div>
                          <div class="input-field">
                        
                          <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end meraki_sm----------------------------->
                   <!-- --------------------------------------- Orbital----------------------------------- -->

                   <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="orbital container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="orbital" style="padding:10px;" >Orbital </h5>
                            <hr>
                          <label for="" class="orbital" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="orbital" name="orbital_sub" id="orbital_sub" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="orbital" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="orbital" name="orbital_manage" id="orbital_manage" value="managed" />
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end orbital--------------------------- -->
                  <!-- --------------------------------------- Duo----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="duo container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="duo" style="padding:10px;" >Duo </h5>
                            <hr>
                          <label for="" class="duo" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="duo" name="duo_sub" id="duo_sub" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="duo" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="duo" name="duo_managed" id="duo_managed" value="managed" />
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end Duo--------------------------- -->
                  <!-- --------------------------------------- ces----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="ces container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="ces" style="padding:10px;" >CES </h5>
                            <hr>
                          <label for="" class="ces" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="ces" name="ces_sub" id="ces" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="ces" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="ces" name="ces_manage" id="ces" value="managed" />
                          
                          </div>
                          <div class="input-field">
                        
                          <input class="form-control ces" name="ces_name"  type="text" placeholder="Name" size="40"/><br>
                          <input class="form-control ces" name="ces_uname"  type="text" placeholder="Username" size="40"/><br>
                          <input class="form-control ces" name="ces_pswd"  type="text" placeholder="Password" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end ces----------------------------->
                   <!-- --------------------------------------- firewall----------------------------------- -->

                   <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="firewall container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="firewall" style="padding:10px;" >CES </h5>
                            <hr>
                          <label for="" class="firewall" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="firewall" name="firewall_sub" id="firewall_sub" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="firewall" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="firewall" name="firewall_manage" id="firewall_manage" value="managed" />
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control ces" name="ces_name"  type="text" placeholder="Name" size="40"/><br>
                          <input class="form-control ces" name="ces_uname"  type="text" placeholder="Username" size="40"/><br>
                          <input class="form-control ces" name="ces_pswd"  type="text" placeholder="Password" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- -----------------------------------------------end of firewall----------------------------->
                  <!-- --------------------------------------- Secure malware analytics----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="secure_malware container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="secure_malware" style="padding:10px;" >Secure Malware Analytics </h5>
                            <hr>
                          <label for="" class="secure_malware" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="secure_malware" name="secure_malware_sub" id="secure_malware_sub" value="subscribed" />
                          &nbsp  &nbsp &nbsp
                          <label for="" class="secure_malware" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="secure_malware" name="secure_malware_managed" id="secure_malware_manage" value="managed" />
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control ces" name="ces_name"  type="text" placeholder="Name" size="40"/><br>
                          <input class="form-control ces" name="ces_uname"  type="text" placeholder="Username" size="40"/><br>
                          <input class="form-control ces" name="ces_pswd"  type="text" placeholder="Password" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- -----------------------------------------------end of secure malware analytics----------------------------->
                  <!-- --------------------------------------- stealthwatchCloud----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="stealthwatch container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="stealthwatch" style="padding:10px;" >Stealthwatch Cloud </h5>
                            <hr>
                          <label for="" class="stealthwatch" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="stealthwatch" name="stealthwatch_sub" id="stealthwatch_sub" value="subscribed"/>
                          &nbsp  &nbsp &nbsp
                          <label for="" class="stealthwatch" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="stealthwatch" name="stealthwatch_managed" id="stealthwatch_manage" value="managed"/>
                          
                          </div>
                          <!-- <div class="input-field">
                        
                          <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                          <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                          </div> -->
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end of stealthwatch----------------------------->
                  <!-- --------------------------------------- Elastic Search----------------------------------- -->

                  <div class="row" >
                    <!-- <div class="col"> -->
                      <div id="showthis_1">
                        <div class="elastic container-secure"  style="border: 1px solid gray; margin-top:10px;">
                          <div class="label-check">
                            <h5 class="elastic" style="padding:10px;" >Elastic Search </h5>
                            <hr>
                          <label for="" class="elastic" style="padding:10px;" >Subscribed</label>
                          <input type="checkbox" class="elastic" name="elastic_sub" id="elastic_sub" value="subscribed"/>
                          &nbsp  &nbsp &nbsp
                          <label for="" class="elastic" style="padding:10px;" >Managed</label>
                          <input type="checkbox" class="elastic" name="elastic_managed" id="elastic_managed" value="managed"/>
                          
                          </div>
                          <div class="input-field">
                        
                          <input class="form-control elastic" name="deploy_name"  type="text" placeholder="Deplyment Name" size="40"/><br>
                          <input class="form-control elastic" name="deploy_id"  type="text" placeholder="Deplyment Id" size="40"/><br>
                          <input class="form-control elastic" name="endpt_url"  type="text" placeholder="Endpoint URL" size="40"/><br>
                          <input class="form-control elastic" name="elastic_api"  type="text" placeholder="Api Key" size="40"/><br>
                          <input class="form-control elastic" name="elastic_region"  type="text" placeholder="Region" size="40"/><br>
                          </div>
                      </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end elastic----------------------------->
                    <!-- --------------------------------------- onelogin----------------------------------- -->

                    <div class="row" >
                        <!-- <div class="col"> -->
                          <div id="showthis_1">
                            <div class="onelogin container-secure"  style="border: 1px solid gray; margin-top:10px;">
                              <div class="label-check">
                                <h5 class="onelogin" style="padding:10px;" >Onelogin </h5>
                                <hr>
                              <label for="" class="onelogin" style="padding:10px;" >Subscribed</label>
                              <input type="checkbox" class="onelogin" name="onelogin_sub" id="onelogin_sub" value="subscribed"/>
                              &nbsp  &nbsp &nbsp
                              <label for="" class="onelogin" style="padding:10px;" >Managed</label>
                              <input type="checkbox" class="onelogin" name="onelogin_managed" id="onelogin_managed" value="managed"/>
                              
                              </div>
                              <!-- <div class="input-field">
                            
                              <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                              <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                              </div> -->
                          </div>
                        </div>
                     
                      </div>
                      <!-- ----------------------------------------------- end of onelogin----------------------------->
                      <!-- --------------------------------------- azuread----------------------------------- -->

                      <div class="row" >
                            <!-- <div class="col"> -->
                            <div id="showthis_1">
                                <div class="azure_ad container-secure"  style="border: 1px solid gray; margin-top:10px;">
                                <div class="label-check">
                                    <h5 class="azure_ad" style="padding:10px;" >Azure AD </h5>
                                    <hr>
                                <label for="" class="azure_ad" style="padding:10px;" >Subscribed</label>
                                <input type="checkbox" class="azure_ad" name="azure_ad_sub" id="azure_ad_sub" value="subscribed"/>
                                &nbsp  &nbsp &nbsp
                                <label for="" class="azure_ad" style="padding:10px;" >Managed</label>
                                <input type="checkbox" class="azure_ad" name="azure_ad_managed" id="azure_ad_managed" value="managed"/>
                                
                                </div>
                                <!-- <div class="input-field">
                                
                                <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                                <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                                </div> -->
                            </div>
                        </div>
                     
                      </div>
                      <!-- ----------------------------------------------- end of azuread----------------------------->
                       <!-- --------------------------------------- sentinelOne----------------------------------- -->

                       <div class="row" >
                        <!-- <div class="col"> -->
                        <div id="showthis_1">
                            <div class="sentinelOne container-secure"  style="border: 1px solid gray; margin-top:10px;">
                            <div class="label-check">
                                <h5 class="sentinelOne" style="padding:10px;" >SentinelOne </h5>
                                <hr>
                            <label for="" class="sentinelOne" style="padding:10px;" >Subscribed</label>
                            <input type="checkbox" class="sentinelOne" name="sentinelOne_sub" id="sentinelOne_sub" value="subscribed"/>
                            &nbsp  &nbsp &nbsp
                            <label for="" class="sentinelOne" style="padding:10px;" >Managed</label>
                            <input type="checkbox" class="sentinelOne" name="sentinelOne_managed" id="sentinelOne_managed" value="managed"/>
                            
                            </div>
                            <!-- <div class="input-field">
                            
                            <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                            <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                            </div> -->
                        </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end of sentinelOne----------------------------->
                      <!-- --------------------------------------- O365----------------------------------- -->

                      <div class="row" >
                        <!-- <div class="col"> -->
                        <div id="showthis_1">
                            <div class="o365 container-secure"  style="border: 1px solid gray; margin-top:10px;">
                            <div class="label-check">
                                <h5 class="o365" style="padding:10px;" >O365 </h5>
                                <hr>
                            <label for="" class="o365" style="padding:10px;" >Subscribed</label>
                            <input type="checkbox" class="o365" name="o365_sub" id="o365_sub" value="subscribed"/>
                            &nbsp  &nbsp &nbsp
                            <label for="" class="o365" style="padding:10px;" >Managed</label>
                            <input type="checkbox" class="o365" name="o365_managed" id="o365_managed" value="managed"/>
                            
                            </div>
                            <div class="input-field">
                            
                            <input class="form-control o365" name="o365_pswd" id="o365_pswd"  type="text" placeholder="Password" size="40"/><br>
                            <!-- <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br> -->
                            </div>
                        </div>
                    </div>
                 
                  </div>
                  <!-- ----------------------------------------------- end of o365----------------------------->
                   <!-- --------------------------------------- cybereason----------------------------------- -->

                   <div class="row" >
                    <!-- <div class="col"> -->
                    <div id="showthis_1">
                        <div class="cybereason container-secure"  style="border: 1px solid gray; margin-top:10px;">
                        <div class="label-check">
                            <h5 class="cybereason" style="padding:10px;" >Cybereason </h5>
                            <hr>
                        <label for="" class="cybereason" style="padding:10px;" >Subscribed</label>
                        <input type="checkbox" class="cybereason" name="cyber_sub" id="cyber_sub" value="subscribed"/>
                        &nbsp  &nbsp &nbsp
                        <label for="" class="cybereason" style="padding:10px;" >Managed</label>
                        <input type="checkbox" class="cybereason" name="cyber_managed" id="cyber_managed" value="managed"/>
                        
                        </div>
                        <!-- <div class="input-field">
                        
                        <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                        <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                        </div> -->
                    </div>
                </div>
             
              </div>
              <!-- ----------------------------------------------- end of cybereason----------------------------->
              <!-- ---------------------------------------proofpoint----------------------------------- -->

              <div class="row" >
                <!-- <div class="col"> -->
                <div id="showthis_1">
                    <div class="proofpoint container-secure"  style="border: 1px solid gray; margin-top:10px;">
                    <div class="label-check">
                        <h5 class="proofpoint" style="padding:10px;" >Proofpoint </h5>
                        <hr>
                    <label for="" class="proofpoint" style="padding:10px;" >Subscribed</label>
                    <input type="checkbox" class="proofpoint" name="proofpoint_sub" id="proofpoint_sub" value="subscribed"/>
                    &nbsp  &nbsp &nbsp
                    <label for="" class="proofpoint" style="padding:10px;" >Managed</label>
                    <input type="checkbox" class="proofpoint" name="proofpoint_managed" id="proofpoint_managed" value="managed"/>
                    
                    </div>
                    <!-- <div class="input-field">
                    
                    <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                    <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                    </div> -->
                </div>
            </div>
         
          </div>
          <!-- ----------------------------------------------- end of proofpoint ----------------------------->
          <!-- ---------------------------------------paloalto----------------------------------- -->

          <div class="row" >
            <!-- <div class="col"> -->
            <div id="showthis_1">
                <div class="paloalto container-secure"  style="border: 1px solid gray; margin-top:10px;">
                <div class="label-check">
                    <h5 class="paloalto" style="padding:10px;" >Paloalto</h5>
                    <hr>
                <label for="" class="paloalto" style="padding:10px;" >Subscribed</label>
                <input type="checkbox" class="paloalto" name="paloalto_sub" id="paloalto_sub" value="subscribed"/>
                &nbsp  &nbsp &nbsp
                <label for="" class="paloalto" style="padding:10px;" >Managed</label>
                <input type="checkbox" class="paloalto" name="paloalto_managed" id="paloalto_managed" value="managed"/>
                
                </div>
                <!-- <div class="input-field">
                
                <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
                <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
                </div> -->
            </div>
        </div>
     
      </div>
      <!-- ----------------------------------------------- end of paloalto----------------------------->
      <!-- ---------------------------------------Ninjapro----------------------------------- -->

      <div class="row" >
        <!-- <div class="col"> -->
        <div id="showthis_1">
            <div class="ninjapro container-secure"  style="border: 1px solid gray; margin-top:10px;">
            <div class="label-check">
                <h5 class="ninjapro" style="padding:10px;" >Ninjapro</h5>
                <hr>
            <label for="" class="ninjapro" style="padding:10px;" >Subscribed</label>
            <input type="checkbox" class="ninjapro" name="ninjapro_sub" id="ninjapro_sub" value="subscribed"/>
            &nbsp  &nbsp &nbsp
            <label for="" class="ninjapro" style="padding:10px;" >Managed</label>
            <input type="checkbox" class="ninjapro" name="ninjapro_managed" id="ninjapro_managed" value="managed"/>
            
            </div>
            <!-- <div class="input-field">
            
            <input class="form-control merakism" name="sm_api"  type="text" placeholder="Api key" size="40"/><br>
            <input class="form-control merakism" name="sm_secret"  type="text" placeholder="Secret" size="40"/><br>
            </div> -->
        </div>
    </div>
 
  </div>
  <!-- ----------------------------------------------- end of paloalto----------------------------->
      
                </div>
              </div>
            </div>

            <!-- #################################### end of controls ################################################ -->
            <!-- ######################################### Contact ################################################### -->
            <div class="contact-detail" style="padding-top: 20px;">  
              <div class="row" style="border:1px solid rgb(101, 98, 98);padding:20px;">
                <h5 class="heading">Contact Details</h5>
                <hr>
                <div class="test" id="add_field">
                  <div class="row" style="border: 1px solid rgb(83, 85, 84);margin:0.5px;">
                    <div class="col-md-8">
                        <div style="margin-top: 8px;">
                            <h6>Point of Contact(Port53)</h6>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div style="margin-top: 8px;">
                            <button type="button" name="add" id="add" class="btn btn-primary" style="padding: 5px;">+ Add More</button>
                        </div>
                    </div>
                  </div>
                  <div class="control-form" id="add_field" style="padding: 15px;border:1px solid gray;margin-top:20px;">
                  
                      <div class="row" style="font-size:13px;padding-bottom:15px;">
                        <div class="col-md-4">
                          <label for="" class="labels">Name</label><br>
                          <input type="text" class="form-control" placeholder="name" name="poc_name">
                        </div>
                        <div class="col-md-4">
                          <label for="" class="labels">Email ID</label><br>
                          <input type="text" class="form-control" placeholder="email" name="poc_email">
                        </div>
                        <div class="col-md-4">
                          <label for="" class="labels">Phone Number</label><br>
                          <input type="text" class="form-control" placeholder="phone number" name="poc_phone">
                        </div>
                      </div>
                      <div class="row" style="font-size:13px;padding-bottom:15px;">
                        <div class="col-md-4">
                          <label for="">Mobile Number</label>
                          <input type="text" class="form-control" placeholder="mobile number" name="poc_mobile">
                        </div>
                        <div class="col-md-4">
                          <label for="">Role</label>
                          <input type="text" class="form-control" placeholder="role" name="poc_role">
                        </div>
                        <div class="col-md-4">
                          <label for="">Title</label>
                          <input type="text" class="form-control" placeholder="title" name="poc_title">
                        </div>
                      </div>
                      <div class="row" style="font-size:13px;padding-bottom:15px;">
                        <div class="col-md-4">
                          <label for="">is_primary</label>
                          <select id="primary_check" class="form-control" name="poc_primary">
                              <option selected>Choose...</option>
                             
                              <option value="true">True</option>
                              <option value="false">False</option>
                            </select>
                        </div>
                      </div>
                
                  </div>

                </div>
                <!-- ##----------------------------client-----------------------------------## -->
                <div class="test" id="add_field_client" style="padding-top:10px;">
                  <div class="row" style="border: 1px solid rgb(83, 85, 84);margin:0.5px;">
                    <div class="col-md-8">
                        <div style="margin-top: 8px;">
                            <h6>Client Contact Details</h6>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div style="margin-top: 8px;">
                            <button type="button" name="add_client" id="add_client" class="btn btn-primary" style="padding: 5px;">+ Add More</button>
                        </div>
                    </div>
                  </div>

                  <div class="control-form" id="add_field" style="padding: 15px;border:1px solid gray;margin-top:20px;">
                  
                    <div class="row" style="font-size:13px;padding-bottom:15px;">
                      <div class="col-md-4">
                        <label for="" class="labels">Name</label><br>
                        <input type="text" class="form-control" placeholder="name" name="c_name">
                      </div>
                      <div class="col-md-4">
                        <label for="" class="labels">Email ID</label><br>
                        <input type="text" class="form-control" placeholder="email" name="c_email">
                      </div>
                      <div class="col-md-4">
                        <label for="" class="labels">Phone Number</label><br>
                        <input type="text" class="form-control" placeholder="phone number" name="c_phone">
                      </div>
                    </div>
                    <div class="row" style="font-size:13px;padding-bottom:15px;">
                      <div class="col-md-4">
                        <label for="">Mobile Number</label>
                        <input type="text" class="form-control" placeholder="mobile number" name="c_mobile">
                      </div>
                      <div class="col-md-4">
                        <label for="">Role</label>
                        <input type="text" class="form-control" placeholder="role" name="c_role">
                      </div>
                      <div class="col-md-4">
                        <label for="">Title</label>
                        <input type="text" class="form-control" placeholder="title" name="c_title">
                      </div>
                    </div>
                    <div class="row" style="font-size:13px;padding-bottom:15px;">
                      <div class="col-md-4">
                        <label for="">is_primary</label>
                        <select id="primary_check" class="form-control" name="c_primary">
                            <option selected>Choose...</option>
                        
                            <option value="true">True</option>
                            <option value="false">False</option>
                          </select>
                      </div>
                    </div>
              
                </div>

                </div>
              </div>
            </div>

            <!-- ####################################### end of contact ############################################## -->
                <!-- ####################################### services ################################################# -->
            <div class="services" style="margin-top: 10px;">
              <div class="row" style="border:1px solid rgb(101, 98, 98);padding:12px;font-size:12px;">
              <div class="row">
              

                  <h5 class="heading">Services</h5>
                  <hr>

                  <div class="col ">
                    <label for="ser_date" class="org_label">Sign Date</label>
                    <input type="date" class="form-control " placeholder="" name="sign_date">
                  </div>
                  <div class="col ">
                    <label for="ser_kickoff" class="org_label">Kickoff Date</label>
                    <input type="date" class="form-control " placeholder="" name="kick_date">
                  </div>
                  <div class="col ">
                    <label for="go-live" class="org_label">Go Live Date</label>
                    <input type="date" class="form-control " placeholder="" name="live_date">
                  </div>

                </div>

                <div class="row" style="margin-top: 10px;">
                  <div class="col-md-4 ">
                    <label for="signed-quarter" class="org_label">Signed Quarter</label>
                    <input type="text" class="form-control " placeholder="Signed Quarter" name="signed_quarter">
                  </div>

                  <div class="col-md-4" >
                    <label for="">Meeting Cadence</label><br>&nbsp;&nbsp;<br>
                    <input type="text" class="form-control " placeholder="Meeting Cadence" name="meeting_cadence">
                    <!-- <select id="primary_check" class="form-control" name="meeting_cadence">
                        <option selected>Choose...</option>
                      
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                      </select> -->
                  </div>

                </div>
              </div>
              </div>

                <!-- ####################################### end of services ################################################# -->
                <!-- ####################################### critical assests ################################################# -->
                <div class="services" style="margin-top: 10px;">
                  <div class="row" style="border:1px solid rgb(101, 98, 98);padding:12px;font-size:12px;">
                  <div class="row">
                  

                      <h5 class="heading">Critical Assets(VMs)</h5>
                      <hr>
  
                      <div class="col ">
                        <label for="assests_name" class="org_label">Name</label>
                        <input type="text" class="form-control " placeholder="Name" id ="asset_name" name="as_name">
                      </div>
                      <div class="col ">
                        <label for="assests_type" class="org_label">Type</label>
                        <input type="text" class="form-control " placeholder="Type" name="assets_type">
                      </div>
                      <div class="col ">
                        <label for="assets_add" class="org_label">IP Address</label>
                        <input type="text" class="form-control " placeholder="IP address" name="assets_ip">
                      </div>
  
                    </div>

                    <div class="row" style="margin-top: 10px;">
                      <div class="col-md-4 ">
                        <label for="contact" class="org_label">Contact</label>
                        <input type="text" class="form-control " placeholder="contact" name="assets_contact">
                      </div>


                    </div>
                  </div>
                  </div>

                <!-- ####################################### end of critical assets ################################################# -->
                


            <div>
              <!-- <button type="button" class="btn btn-outline-primary" style="color:white;border:1px solid rgb(35, 95, 173);margin-top:20px;">Submit</button> -->
              <input type="submit"  class="btn btn-outline-primary" style="color:white;border:1px solid rgb(35, 95, 173);margin-top:20px;" >
            </div>
          </form>
        </div>
    
    </div>
  
  </div>

{% endblock %}



<script>
            $(function () {
              $('.secure_sh').hide();
        
              //show it when the checkbox is clicked
              $('input[name="securex"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.secure_sh').fadeIn();
                      $('.secure_sh').fadeIn();
                  } else {
                      $('.secure_sh').hide();
                      $('.secure_sh').hide();
                  }
              });
          });
        
          </script>
        
          <script>
            $(function () {
              $('.secure_pnt').hide();
        
              //show it when the checkbox is clicked
              $('input[name="secure_endpoint"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.secure_pnt').fadeIn();
                      $('.secure_pnt').fadeIn();
                  } else {
                      $('.secure_pnt').hide();
                      $('.secure_pnt').hide();
                  }
              });
          });
        
          </script>
        
          
          <script>
            $(function () {
              $('.umb').hide();
        
              //show it when the checkbox is clicked
              $('input[name="umbrella"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.umb').fadeIn();
                      $('.umb').fadeIn();
                  } else {
                      $('.umb').hide();
                      $('.umb').hide();
                  }
              });
          });
        
          </script>
          <script>
            $(function () {
              $('.umb_invest').hide();
        
              //show it when the checkbox is clicked
              $('input[name="umbrella_invest"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.umb_invest').fadeIn();
                      $('.umb_invest').fadeIn();
                  } else {
                      $('.umb_invest').hide();
                      $('.umb_invest').hide();
                  }
              });
          });
        
          </script>

          <script>
            $(function () {
              $('.merakimx').hide();
        
              //show it when the checkbox is clicked
              $('input[name="meraki_mx"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.merakimx').fadeIn();
                      $('.merakimx').fadeIn();
                  } else {
                      $('.merakimx').hide();
                      $('.merakimx').hide();
                  }
              });
          });
        
          </script>
          
          <script>
            $(function () {
              $('.merakism').hide();
        
              //show it when the checkbox is clicked
              $('input[name="meraki_sm"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.merakism').fadeIn();
                      $('.merakism').fadeIn();
                  } else {
                      $('.merakism').hide();
                      $('.merakism').hide();
                  }
              });
          });
        
          </script>
          
          <script>
            $(function () {
              $('.orbital').hide();
        
              //show it when the checkbox is clicked
              $('input[name="orbital"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.orbital').fadeIn();
                      $('.orbital').fadeIn();
                  } else {
                      $('.orbital').hide();
                      $('.orbital').hide();
                  }
              });
          });
        
          </script>
          <script>
            $(function () {
              $('.duo').hide();
        
              //show it when the checkbox is clicked
              $('input[name="duo"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.duo').fadeIn();
                      $('.duo').fadeIn();
                  } else {
                      $('.duo').hide();
                      $('.duo').hide();
                  }
              });
          });
        
          </script>

          <script>
            $(function () {
              $('.ces').hide();
        
              //show it when the checkbox is clicked
              $('input[name="ces"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.ces').fadeIn();
                      $('.ces').fadeIn();
                  } else {
                      $('.ces').hide();
                      $('.ces').hide();
                  }
              });
          });
        
          </script>

          <script>
            $(function () {
              $('.firewall').hide();
        
              //show it when the checkbox is clicked
              $('input[name="firewall"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.firewall').fadeIn();
                      $('.firewall').fadeIn();
                  } else {
                      $('.firewall').hide();
                      $('.firewall').hide();
                  }
              });
          });
        
          </script>
          <script>
            $(function () {
              $('.secure_malware').hide();
        
              //show it when the checkbox is clicked
              $('input[name="secure_malware"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.secure_malware').fadeIn();
                      $('.secure_malware').fadeIn();
                  } else {
                      $('.secure_malware').hide();
                      $('.secure_malware').hide();
                  }
              });
          });
        
          </script>

          <script>
            $(function () {
              $('.stealthwatch').hide();
        
              //show it when the checkbox is clicked
              $('input[name="stealthwatch"]').on('click', function () {
                  if ($(this).prop('checked')) {
                      $('.stealthwatch').fadeIn();
                      $('.stealthwatch').fadeIn();
                  } else {
                      $('.stealthwatch').hide();
                      $('.stealthwatch').hide();
                  }
              });
          });
        
          </script>
          <script>

          $(function () {
            $('.elastic').hide();
      
            //show it when the checkbox is clicked
            $('input[name="elastic"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.elastic').fadeIn();
                    $('.elastic').fadeIn();
                } else {
                    $('.elastic').hide();
                    $('.elastic').hide();
                }
            });
        });
      
        </script>

        <script>

          $(function () {
            $('.onelogin').hide();
      
            //show it when the checkbox is clicked
            $('input[name="onelogin"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.onelogin').fadeIn();
                    $('.onelogin').fadeIn();
                } else {
                    $('.onelogin').hide();
                    $('.onelogin').hide();
                }
            });
        });
      
        </script>

        <script>

          $(function () {
            $('.azure_ad').hide();
      
            //show it when the checkbox is clicked
            $('input[name="azure_ad"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.azure_ad').fadeIn();
                    $('.azure_ad').fadeIn();
                } else {
                    $('.azure_ad').hide();
                    $('.azure_ad').hide();
                }
            });
        });
      
        </script>

        
        <script>

          $(function () {
            $('.o365').hide();
      
            //show it when the checkbox is clicked
            $('input[name="o365"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.o365').fadeIn();
                    $('.o365').fadeIn();
                } else {
                    $('.o365').hide();
                    $('.o365').hide();
                }
            });
        });
      
        </script>

        <script>

          $(function () {
            $('.sentinelOne').hide();
      
            //show it when the checkbox is clicked
            $('input[name="sentinelOne"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.sentinelOne').fadeIn();
                    $('.sentinelOne').fadeIn();
                } else {
                    $('.sentinelOne').hide();
                    $('.sentinelOne').hide();
                }
            });
        });
      
        </script>
        
        <script>

          $(function () {
            $('.cybereason').hide();
      
            //show it when the checkbox is clicked
            $('input[name="cybereason"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.cybereason').fadeIn();
                    $('.cybereason').fadeIn();
                } else {
                    $('.cybereason').hide();
                    $('.cybereason').hide();
                }
            });
        });
      
        </script>
        <script>

          $(function () {
            $('.proofpoint').hide();
      
            //show it when the checkbox is clicked
            $('input[name="proofpoint"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.proofpoint').fadeIn();
                    $('.proofpoint').fadeIn();
                } else {
                    $('.proofpoint').hide();
                    $('.proofpoint').hide();
                }
            });
        });
      
        </script>

        <script>

          $(function () {
            $('.paloalto').hide();
      
            //show it when the checkbox is clicked
            $('input[name="paloalto"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.paloalto').fadeIn();
                    $('.paloalto').fadeIn();
                } else {
                    $('.paloalto').hide();
                    $('.paloalto').hide();
                }
            });
        });
      
        </script>

        <script>

          $(function () {
            $('.ninjapro').hide();
      
            //show it when the checkbox is clicked
            $('input[name="ninja_pro"]').on('click', function () {
                if ($(this).prop('checked')) {
                    $('.ninjapro').fadeIn();
                    $('.ninjapro').fadeIn();
                } else {
                    $('.ninjapro').hide();
                    $('.ninjapro').hide();
                }
            });
        });
      
        </script>
        
            <script>
              [".collapsed-menu"].forEach((val) => {
                Array.prototype.forEach.call(document.querySelectorAll(val), (ele) => {
                  ele.children[0].onclick = (e) => {
                    ele.classList.toggle("toggled");
                  };
                });
              });
              
            </script>
        
            <script>
              $(document).ready(function(){
                  var i = 1;
                 
                  $("#add").click(function(){
                   
                   i++;
                      $('#add_field').append('<div class="row" id="row'+i+'" style="border:1px solid gray;padding:10px;margin-top:10px;margin-left:2px;margin-right:2px;">\
                                              <div class=col-md-10>\
                                              <div class="row" style="font-size:13px;padding-bottom:15px;" >\
                                                  <div class="col">\
                                                      <label for="">Name</label>\
                                                      <input type="text" class="form-control" placeholder="name" name="poc_name">\
                                                  </div>\
                                                  <div class="col">\
                                                      <label for="">Email ID</label>\
                                                      <input type="text" class="form-control" placeholder="phone number" name="poc_email">\
                                                  </div>\
                                                  <div class="col">\
                                                      <label for="">Phone Number</label>\
                                                      <input type="text" class="form-control" placeholder="phone number" name="poc_phone">\
                                                  </div>\
                                              </div>\
                                              <div class="row" style="font-size:13px;padding-bottom:15px;">\
                                                  <div class="col">\
                                                      <label for="">Mobile Number</label>\
                                                      <input type="text" class="form-control" placeholder="mobile number" name="poc_mobile">\
                                                  </div>\
                                                  <div class="col">\
                                                      <label for="">Role</label>\
                                                      <input type="text" class="form-control" placeholder="role" name="poc_role">\
                                                  </div>\
                                                  <div class="col">\
                                                      <label for="">Title</label>\
                                                      <input type="text" class="form-control" placeholder="title" name="poc_title">\
                                                  </div>\
                                              </div>\
                                              <div class="row" style="font-size:13px;padding-bottom:15px;">\
                                                  <div class="col-md-4">\
                                                      <label for="">is_primary</label>\
                                                      <select id="primary_check" class="form-control" name="poc_primary">\
                                                          <option selected>Choose...</option>\
                                                          <option value="true">True</option>\
                                                          <option value="false">False</option>\
                                                      </select> \
                                                  </div>\
                                              </div>\
                                          </div>\
                                          <div class="col-md-2">\
                                              <button type="button" name="remove" id="'+i+'" class="btn btn-danger btn_remove">X</button>\
                                          </div>\
                                          </div>'
                                              ); 
                    });
                  $(document).on('click', '.btn_remove', function(){ 
                  
                      var button_id = $(this).attr("id");    
                      $('#row'+button_id+'').remove(); 
                    });
                  
                  });
          </script>
        
        
          <script>
            $(document).ready(function(){
                var i = 1;
               
                $("#add_client").click(function(){
                 
                 i++;
                    $('#add_field_client').append('<div class="row" id="row'+i+'" style="border:1px solid gray;padding:10px;margin-top:10px;margin-left:2px;margin-right:2px;">\
                      <div class=col-md-10>\
                      <div class="row" style="font-size:13px;padding-bottom:15px;" >\
                          <div class="col">\
                              <label for="">Name</label>\
                              <input type="text" class="form-control" placeholder="name" name="c_name">\
                          </div>\
                          <div class="col">\
                              <label for="">Email ID</label>\
                              <input type="text" class="form-control" placeholder="phone number" name="c_email">\
                          </div>\
                          <div class="col">\
                              <label for="">Phone Number</label>\
                              <input type="text" class="form-control" placeholder="phone number" name="c_phone">\
                          </div>\
                      </div>\
                      <div class="row" style="font-size:13px;padding-bottom:15px;">\
                          <div class="col">\
                              <label for="">Mobile Number</label>\
                              <input type="text" class="form-control" placeholder="mobile number" name="c_mobile">\
                          </div>\
                          <div class="col">\
                              <label for="">Role</label>\
                              <input type="text" class="form-control" placeholder="role" name="c_role">\
                          </div>\
                          <div class="col">\
                              <label for="">Title</label>\
                              <input type="text" class="form-control" placeholder="title" name="c_title">\
                          </div>\
                      </div>\
                      <div class="row" style="font-size:13px;padding-bottom:15px;">\
                          <div class="col-md-4">\
                              <label for="">is_primary</label>\
                              <select id="primary_check" class="form-control" name="c_primary">\
                                  <option selected>Choose...</option>\
                                  <option value="true">True</option>\
                                  <option value="false">False</option>\
                              </select> \
                          </div>\
                      </div>\
                  </div>\
                  <div class="col-md-2">\
                      <button type="button" name="remove" id="'+i+'" class="btn btn-danger btn_remove">X</button>\
                  </div>\
                  </div>'
                                            ); 
                  });
                $(document).on('click', '.btn_remove_client', function(){ 
                
                    var button_id = $(this).attr("id");    
                    $('#row'+button_id+'').remove(); 
                  });
                
                });
        </script>
