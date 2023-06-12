from django.urls import path

from account import views

urlpatterns=[
    path('',views.base,name='base'),
    path('add_user',views.add_user,name='add_user'),

    path('client_form',views.client_form,name='client_form'),
    path('add_client',views.add_client,name='add_client'),
    path('add_user/<str:id>',views.add_user,name='add_user'),
    path('user_dt',views.user_dt,name='user_dt'),

]
#####################################
from django.shortcuts import render,redirect,HttpResponse
from account.models import Employee
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def base(request):
    return render(request,'emp.html')

def add_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        role = request.POST['role']
        title = request.POST['title']
    
        dt = Employee.objects.create(name=name,email=email,phone=phone,mobile=mobile,role=role,title=title)
        print(dt)
        dt.save()
    return redirect("base")

def client_form(request):
    dt = Employee.objects.all()
    context={'dt':dt}
    return render(request,'client_form.html',context)

def user_dt(request):
    print("working")
   
    user_dt = Employee.objects.all()
    data = serializers.serialize('json',user_dt)
    return HttpResponse(data,content_type="application/json")

def add_user(request,id):
    print("working")
    print("id is===",id)
    user_dt = Employee.objects.filter(id=id)
    data = serializers.serialize('json',user_dt)
    return HttpResponse(data,content_type="application/json")



def add_client(request,id):
    return render(request,'client_form.html')
    #####################################
    
   {%load static %}

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <title>Hello, world!</title>
  </head>
  <body>
    <div class="card" style="padding-left: 40px;">
        <div class="card-title">
            ADD CLIENTS
        </div>
        <form action="{% url 'add_client' %}" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <h5>Organization</h5>
                    <!-- ####################################### organization ##################################### -->
                    <div class="row" >
        
                      <div class="col-sm-4 ">
                        <label for="org_id" class="org_label">Organization ID(Umbrella)</label>
                        <input type="text" class="form-control " placeholder="organization Id" name="org_id" id="org_id">
                      </div>
                      <div class="col-sm-4 ">
                        <label for="jira_id" class="org_label">Jira ID</label>
                        <input type="text" class="form-control " placeholder="jira Id" name="jira_id" id="jira_id">
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-4 ">
                        <label for="org_name" class="org_label">Organization Name</label>
                        <input type="text" class="form-control " placeholder="Organization name" name="org_name">
                      </div>
                      <div class="col-sm-4">
                        <label for="timezone" class="org_label">Timezone</label>
                        <!-- <input type="text" class="form-control " placeholder="timezone" name="timez"> -->
                        <select id="timez" class="form-control" name="timez">
                          <option selected>Choose...</option>
                          <option value="Eastern Time">Eastern Time</option>
                          <option value="Eastern Standard Time">Eastern Standard Time</option> 
                          <option value=" Eastern Daylight Time"> Eastern Daylight Time</option> 

                        
                          
                          
                        </select>
                      </div>
        
                    </div>
                    <!-- ############################## end of organization ########################################### -->
                    <div class="row" id="add_field">
                        <div class="col-md-6" >
                            <label for="inputStatus">Point of contact</label>
                                <select id="poc" class="form-control-sm custom-select">
                                    <option selected disabled>Choose a poc</option>
                                    {% for i in dt%}
                                    <option value="{{i.id}}">{{i.name}}</option>
                                    {% endfor %}
                                </select>
                        </div>
                        
                        <div class="col-md-6">
                            <div class="form-group" id="user_data">
                              
                            </div>
                    </div>
                    <div style="margin-top: 8px;">
                         <button type="button" name="add" id="add_" class="btn btn-primary" style="padding: 5px;">+ Add More</button>
                    </div>
                    </div>
                    

                 
        

        </form>

    </div>

   
    


    <!-- Optional JavaScript; choose one of the two! -->
    <!-- <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script> -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>



    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
    -->
    <!-- <script src="{% static 'main.js' %}"></script> -->
<script>
    var $j = jQuery.noConflict();
    $(document).ready(function(){
    
        $("#poc").change(function () {
            const uId = $(this).val();  // get the selected subject ID from the HTML dropdown list 
            $.ajax({                       // initialize an AJAX request
                type: "POST",
                url: "add_user/"+uId,
                data: {
                    'id': uId,       // add the country id to the POST parameters
                    'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (data) {   // `data` is from `get_topics_ajax` view function
                    console.log(data)
                    
                    let html_data = '';
                    data.forEach(function (data) {
                        html_data += `<input type="text" class="form-control" placeholder="name" name="poc_name" value=${data.fields.name}>`
                    });
                    $("#user_data").html(html_data); // replace the contents of the topic input with the data that came from the server
                }
            });
        });
    });
    // ###############################################
    
    $(document).ready(function(){
        var i = 1;
       
        $("#add_").click(function(){
            $.ajax({                       // initialize an AJAX request
                type: "POST",
                url: "user_dt",
                data: {
                   
                    'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
                },
               
                success: function (data) {   // `data` is from `get_topics_ajax` view function
                    console.log(data)
                    html_dt += `<div class="col-md-6" id="row'+i+'"><select id="poc" class="form-control-sm custom-select">\
                        <option selected disabled>Choose a poc</option>\
                        <option value="${data.pk}">${name}</option>\
                            </select></div>`
                    
                    let name=[]

                    for (let j=0;j<data.length;j++){
                        console.log("===",data[j]['fields']['name'])
                        name.push(data[j]['fields']['name'])
                        html_dt += `<div class="col-md-6" id="row'+i+'"><select id="poc" class="form-control-sm custom-select">\
                            <option selected disabled>Choose a poc</option>\
                            <option value="${data.pk}">${name}</option>\
                                </select></div>`
                    }
                    console.log("-name-",name)
                   
                    $("#add_field").append(html_dt);
                    
                    
                }
            });
         
          });
        $(document).on('click', '.btn_remove', function(){ 
        
            var button_id = $(this).attr("id");    
            $('#row'+button_id+'').remove(); 
          });
        
        });
    // #####################################
    
</script>
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
  </body>
</html>

##############################################################
var $j = jQuery.noConflict();
$(document).ready(function(){

    $("#poc").change(function () {
        const uId = $(this).val();  // get the selected subject ID from the HTML dropdown list 
        $.ajax({                       // initialize an AJAX request
            type: "POST",
            url: "add_user/"+uId,
            data: {
                'id': uId,       // add the country id to the POST parameters
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {   // `data` is from `get_topics_ajax` view function
                console.log(data)
                
                let html_data = '';
                data.forEach(function (data) {
                    html_data += `<input type="text" class="form-control" placeholder="name" name="poc_name" value=${data.fields.name}>`
                });
                $("#user_data").html(html_data); // replace the contents of the topic input with the data that came from the server
            }
        });
    });
});
// ###############################################

$(document).ready(function(){
    var i = 1;
   
    $("#add").click(function(){
     
     i++;
        $('#add_field').append('<div class="row" id="row'+i+'" style="border:1px solid gray;padding:10px;margin-top:10px;margin-left:2px;margin-right:2px;">\
                                <div class=col-md-6>\
                                    <select id="poc" class="form-control-sm custom-select">\
                                        <option selected disabled>Choose a poc</option>\
                                        {% for i in dt%}\
                                        <option value="{{i.id}}">{{i.name}}</option>\
                                        {% endfor %}\
                                    </select>\
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
// #####################################


.client_card{
    color:#fff;
    background-color:#222323b7;
}
#card-title{
    font-family: 'Lato', sans-serif;
    font-family: 'Open Sans', sans-serif;
    font-family: 'Poppins', sans-serif;
}
select:required:invalid {
    color: gray;
}
option[value=""][disabled] {
    display: none;
}
option {
    color: black;
}
.org_label{
    padding-bottom:20px;
}
:root {
    font-family: "Oxygen", sans-serif;
    --color-0: #FFFFFF !important;
    --color-1: #C8D5E9 !important;
    --color-2: #2196F3 !important;
    --color-3: #505152 !important;
    --accent-color: #1EC0CA;
    --bg-0: #3586A5 !important;
    --bg-1: #C5D4E5 !important;
    --bg-2: #EDF4FF !important;
    --text-shadow: rgba(255, 255, 255, 0.738) !important;
}
.material-symbols-rounded {
    font-family: "Material Symbols Rounded";
}
@import url("https://fonts.googleapis.com/css2?family=Oxygen:wght@300&display=swap");
.wraper {
    display: flex;
}
.collapsed-menu {
    position: relative;
    overflow: hidden;
    max-height: 50px;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    padding: 0;
    transition: max-height 0.2s ease;
    border: 1px solid rgba(216, 210, 210, 0.2);
    border-radius: 8px;
}
.collapsed-menu.toggled {
    max-height: 1000px;
}
.collapsed-menu > .collapsed-menu-btn span {
    transform: rotate(-90deg);
}
.collapsed-menu.toggled > .collapsed-menu-btn span {
    transform: rotate(0);
}
.collapsed-menu .collapsed-menu-list {
    list-style-type: none;
    padding-top: 1.2em;
    padding-right: 2.2em;
    margin: 0;
}
.styled-link {
    display: flex !important;
    justify-content: flex-end !important;
    flex-direction: row-reverse !important;
    cursor: pointer;
    position: relative;
    gap: 0.2em;
    padding-top:12px;
    padding-left: 30px;
    text-decoration: none;
    color: #EBEDF0;
}
.styled-link:before {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0;
    content: " ";
    border-radius: 8px;
    transition: all 0.2s ease-in-out;
}
.styled-link:hover:before {
    opacity: 0.2;
    border-radius: 8px;
}
.styled-link:active:before {
    opacity: 0.4;
    border-radius: 2px;
}
.styled-link *, .styled-link *:before, .styled-link *::after {
    transition: 0.2s ease-in-out;
    user-select: none;
}
.styled-link span {
    padding: 2px;
    font-size: 18px;
}
.styled-link p, .styled-link span {
    vertical-align: middle;
}
.styled-link p {
    opacity: 0.8;
    position: relative;
}
.styled-link p:before {
    position: absolute;
    content: " ";
    width: 0%;
    border-bottom: 1px solid var(--color-0);
    height: 100%;
    margin: 0 49%;
}
.styled-link:hover span {
    color: #fff;
}
.styled-link:hover p {
    opacity: 1;
    color: #fff;
}
.styled-link:hover p:before {
    width: 60%;
    margin: 0 20%;
}
.org_label{
    font-size: 14px;
}
.labels{
    padding-bottom: 5px;
}
.form-control{
    background: rgba(200, 207, 200, 0.575);
    border-color: #505152;
}
select.form-control{
    background: rgba(102, 104, 102, 0.379);
    border-color: #505152;
    outline: 1px solid #2E2F30;
}
.heading{
    color: #1D72E2;
}
.secure_sh,.secure_pnt {
    padding-top: 5px;
    background-color: #19191A;
}
.label-check{
    padding: 10px;
}
.input-field{
    padding: 10px;
}

/* ############ */
.multiselect {
    width: 200px;
  }
  
  .selectBox {
    position: relative;
  }
  
  .selectBox select {
    width: 100%;
    font-weight: bold;
  }
  
  .overSelect {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
  }
  
  #checkboxes {
    display: none;
    border: 1px #dadada solid;
  }
  
  #checkboxes label {
    display: block;
  }
  
  #checkboxes label:hover {
    background-color: #1e90ff;
  }
  
  
