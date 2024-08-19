#!C:/Users/USER/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src='https://kit.fontawesome.com/4c729db828.js' crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js" integrity="sha512-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
   
    <title>Gym Location and Schedule</title>
    <style>
      
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&display=swap');

*{
    margin: 0%;
    padding: 0%;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
    color: #E1E2E4;
    list-style: none;

}

body{
    background-color: #787c7f;
    overflow-x: hidden;
}

.header{
    height: 100vh;
    width: 100%;
}

.navbar{
    padding: 15px 18px !important;
}

.logo
{
    font-weight: 600;
    color: #E1E2E4 !important;
}


.logo:hover
{
    font-weight: 600;
    color: rgb(57, 255, 123) !important;
}

.nav-item .nav-link {
    color: #E1E2E4;
    font-size: 14px;
    font-weight: 500;
    position: relative;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0px;
    background-color:rgb(57, 255, 123);
    width: 0%; 
    height: 3px;
    transition: width 0.4s ease-in-out; }

.nav-link:hover::after { 
    width: 100%; 
}



.nav-link:hover {
    color: rgb(57, 255, 123); /* change color on hover */
}

.nav-link.active {
    color: #696e71; /* change color on active state */
}
.nav-item {
    margin: 0px 10px;
}

.btn-navbar:hover{
    background-color: transparent;
    color: rgb(57, 255, 123);
    border : 1px solid rgb(57, 255, 123);
    transition: 0.2s ease;
}


.btn-navbar{
    display: inline-block;
    padding: 10px 43px;
    border: 1px solid rgb(36, 193, 255);
    color: #e1e2e4;;
    border-radius: 50px;
    text-decoration: none;
    font-size:14px ;
    font-weight: 600;
    background-color: rgb(36, 193, 255);
}

/*home start */
.content-home2{
    height:90vh;
    width: 100%;
    display:flex;
    justify-content: space-between;
    align-items: center;
}

.home-heading{
    font-size: 50px;
    font-weight: 700;
    line-height: 74px;
}
.home-span{
    color: rgb(57, 255, 123);
}
.para-home{
    font-size: 13px;
    font-weight: 500;
    color: #E1E2E4;
    max-width: 400px;
    line-height: 24px;
    margin: 14px 0px;
}

.home-links{
    display: inline-block;
    text-decoration: none;
    color: #E1E2E4;
    border: 1px solid rgb(36, 193, 255);
    background-color: rgb(36, 193, 255);
    margin: 20px 0px;
    margin-right: 7px;
    border-radius: 50px;
    padding: 10px 37px;
    font-size: 14px;
    font-weight: 600;
    transition: 0.2s ease;
}
.btn-2{
    border: 1px solid #E1E2E4;
    color: #E1E2E4;
    background-color: transparent;
}

.box-container2{
    background-color: #787c7f;
}

.home-links:hover{
    background-color: transparent;
    color:rgb(57, 255, 123) ;
    border: 1px solid rgb(57, 255, 123) !important;
}
.img-home{
    margin-right: 20px;
    width: 500px;
    height: 500px;
}

/* about us */
.about-us-container{
    width: 100%;
    height: 80vh;
}

.about-us{
    width: 100%;
    height: 320px;
    background-color: #696e71;
    margin-top: 200px;
    position: relative;

}

.content-about{
    padding: 10px 30px ;
}
.heading-about{
    font-size: 30px;
    font-weight: bold;
    letter-spacing: 1px;
    color: #E1E2E4;
    margin: 10px 0px;
    position: relative;
}

.heading-about::after{
    content: '';
    position:absolute;
    left: 0px;
    bottom: -0px;
    background-color: rgb(57, 255, 123);
    width: 46px;
    height: 2px;
}

.para-about{
    font-size: 13px;
    font-weight: 500;
    color: #e1e2e4;;
    line-height:21px;
    margin: 25px 0px;
}



.img-about{
    height: 420px;
    position:absolute;
    width:50%;
    top: -36px;
    right: 20px;

}

/*product sectioncs*/
.product-category{
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 4px;
}
 .heading-product{
    font-size: 34px;
    color: rgb(57, 255, 123);
    margin-bottom: 120px;
    position: relative;
 }

 .heading-product::after{
    content: '';
    position: absolute;
    left: 0px;
    bottom: -8px;
    background-color: #E1E2E4;
    width: 56px;
    height: 2px;
 }
 .card-product{
    padding: 14px 10px;
    background-color: #696e71 !important;


 }
 .img-card{
    height: 190px !important;


 }
.card-title {
    color:#E1E2E4;
    font-size: 18px;
    width: 100%;
    border-bottom: 1px solid rgb;
    padding: 5px 0px;
    margin: 10px 0px;
    margin-bottom: 20px !important;
}
.card-text{
    color: rgba(255, 255, 255, 0.873);
    font-size :12px;
    line-height: 22px;
}
.btn-product-ctg{
    color: rgb(255, 129, 57);
    text-decoration: none;
    font-size:13px;
    text-transform: uppercase;

}

.btn-product-ctg:hover {
    color: rgb(250, 183, 144);
}
.btn-product-prg{
    color: rgb(255, 129, 57);
    text-decoration: none;
    font-size:13px;
    text-transform: uppercase;

}

.btn-product-prg:hover {
    color: rgb(250, 183, 144);
}
.btn-prev ,.btn-next{
color: rgb(250, 183, 144);
}


.button-left{
    position: absolute;
    left: 20px;
    padding: 10px 12px;
    color: #100f10;
    border-radius:30px;
    background-color: #2c2c2c;
    font: 18px;
}

.button-right{
    position: absolute;
    right: 20px;
    padding: 10px 12px;
    color: #100f10;
    border-radius:30px;
    background-color: #2c2c2c;
    font: 18px;
}

.button-right:hover{
    color: #E1E2E4;
}
.button-left:hover{
    color: #E1E2E4;
}
/*PRODUCT SECTION*/

.testiomonial{
    width: 100%;
    height: 100vh;
    padding: 20px;
    margin-top: 60px;
}

.heading-testimonial{
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #E1E2E4;
    margin-bottom: 35px;
}
.heading-testimonial .styling{
    color: rgb(57, 255, 123);
}

.para-testimonial{
    color:#E1E2E4;
    font-size: 15px;
    letter-spacing: 1px;
    text-align: center !important;
    margin: 12px auto;
    line-height: 25px;
}

.container-clients{
    margin: 100px 0px 30px 0px;
    

}

.container-content {
    width: 90%;
    height: 500px;
    background-color: #696e71; /* changed to black */
    margin: 30px;
    padding: 30px;
    text-align: end;
    border-radius: 5px;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.rating {
    display: flex;
    align-items: center;
  }
  
  .star  {
    font-size: 18px;
    color: #F7DC6F; /* golden color */
    margin-right: 5px;
  }

  .stars {
    font-size: 18px;
    color: #F7DC6F; /* golden color */
    margin-right: 5px;
  }

  .container-clients {
    padding-left: 130px; /* Adjust this value as needed */
}

.stars i {
    color: gold;
}
.product-link{
    text-decoration: none

}
.product-link:hover{
    text-decoration: none
    color(srgb rgb(13, 255, 62) green blue)
}
/* Contact Us Section */
/* Contact Us Section */
/* Contact Us Section */
/* Contact Us Section */
.contact-us {
    background-color: #696e71;
    color: #fff;
    padding: 80px 0;
}

.contact-info {
    padding-right: 50px; /* Adjust spacing */
}

.heading-contact {
    font-size: 36px;
    font-weight: 700;
    color: rgb(57, 255, 123);
    margin-bottom: 30px;
    position: relative;
}

.heading-contact::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -10px;
    background-color: rgb(57, 255, 123);
    width: 60px;
    height: 4px;
}

.para-contact {
    font-size: 18px;
    font-weight: 500;
    line-height: 28px;
    margin-bottom: 30px;
}

.contact-list {
    list-style: none;
    padding: 0;
}

.contact-list li {
    margin-bottom: 20px;
    position: relative;
    padding-left: 30px;
    font-size: 16px;
    line-height: 28px;
}

.contact-list li i {
    position: absolute;
    left: 0;
    top: 2px;
    font-size: 20px;
    color: rgb(57, 255, 123);
}

.contact-form {
    background-color: #696e71;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 20px #787c7f;
}

.drop{
    background-color: #787c7f;
    color: #fff;
}
.dd{
     background-color: #787c7f;
}

.contact-form .form-group {
    margin-bottom: 20px;
}

.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
    background-color: rgba(255, 255, 255, 0.1);
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 12px;
    width: 100%;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

.contact-form textarea {
    resize: none;
    height: 120px;
}

.contact-form textarea:focus,
.contact-form textarea:active {
    background-color: rgba(255, 255, 255, 0.5); 
}

.contact-form input::placeholder,
.contact-form textarea::placeholder {
    color: #fff; /* Placeholder text color */
}

.btn-contact {
    background-color: rgb(57, 255, 123);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 600;
    text-transform: uppercase;
    transition: background-color 0.3s ease;
}

.btn-contact:hover {
    background-color: transparent;
}
.btn-send-message {
    display: inline-block;
    padding: 10px 43px;
    border: 1px solid rgb(57, 255, 123);
    color: white;
    border-radius: 50px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    background-color: rgb(57, 255, 123);
    transition: background-color 0.2s, color 0.2s, border-color 0.2s;
}

.btn-send-message:hover {
    background-color: transparent;
    color: #E1E2E4;
    border-color: rgb(57, 255, 123);
}
.num-contact{
            text-decoration: none;
            color: #a7a7a7;
        }

/* Footer Section */
.footer {
    background-color: #696e71;
    color: #E1E2E4;
    padding: 50px 0;
    font-size: 14px;
    font-weight: 400;
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.footer-logo {
    font-size: 24px;
    font-weight: 700;
    color: rgb(57, 255, 123);
    margin-bottom: 20px;
}

.footer-about {
    max-width: 400px;
    line-height: 24px;
}

.footer-links {
    list-style: none;
    padding: 0;
}

.footer-links li {
    margin-bottom: 10px;
}

.footer-links a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-links a:hover {
    color: rgb(57, 255, 123);
}

.footer-social {
    margin-top: 20px;
}

.footer-social a {
    display: inline-block;
    margin-right: 15px;
    color: #fff;
    font-size: 20px;
    transition: color 0.3s ease;
}

.footer-social :hover {
    color: rgb(57, 255, 123);
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 20px;
    padding-top: 20px;
    text-align: center;
}

.footer-bottom p {
    margin: 0;
}

/*--BMI--*/


.bmi-calculator {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.bmi-calculator h2 {
    margin-bottom: 20px;
}

.bmi-calculator label {
    display: block;
    margin-bottom: 10px;
}

.bmi-calculator input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.bmi-calculator button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    background-color: #28a745;
    color: #fff;
    cursor: pointer;
}

.bmi-calculator button:hover {
    background-color: #218838;
}

#result {
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
}

        /* Add your existing styles here */
        #map {
            height: 400px;
            width: 100%;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            margin-bottom: 20px;
            color: black;
            border: 2px solid #ddd; /* Border around the table */
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #696e71;
            border-right: 1px solid #696e71; /* Border between columns */
        }
        th {
            background-color: black;
        }
        tr:nth-child(even) {
            background-color: black;
        }
        tr:hover {
            background-color: black;
        }
        /* Remove right border from last cell in each row */
        td:last-child {
            border-right: none;
        }

    </style>
    <!-- Replace YOUR_API_KEY with your actual Google Maps API key -->
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdADSFbdC3lyzdDTnSB4_T4MgjbLEEPn4&callback=initMap" async defer></script>
    <script>
        // Initialize and add the map
        function initMap() {
            // The location of Red Muscle Gym
            const gymLocation = { lat: 11.023463, lng: 77.017757 };
            // The map, centered at Red Muscle Gym
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 15,
                center: gymLocation,
            });
            // The marker, positioned at Red Muscle Gym
            const marker = new google.maps.Marker({
                position: gymLocation,
                map: map,
            });
        }
    </script>
</head>
<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container">
          <a class="navbar-brand logo text-uppercase" href="./index.py">The Red Muscle Gym</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="./index.py">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="./aboutus.py">About Us</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown"  data-bs-toggle="dropdown" aria-expanded="false">
                    Services
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" href="./calisthenics.py">Calisthenics</a></li>
                    <li><a class="dropdown-item" href="./weight.py">Weight Loss & Weight Gain</a></li>
                    <li><a class="dropdown-item" href="./bodybuilding.py">Bodybuilding</a></li>
                    <li><a class="dropdown-item" href="./powerlifting.py">Powerlifting</a></li>
                    <li><a class="dropdown-item" href="./sports-specific.py">Sport-Specific Training</a></li>
                    <li><a class="dropdown-item" href="./zumba.py">Zumba Dance Training</a></li>
                </ul>
            </li>
              <li class="nav-item">
                <a class="nav-link" href="./locations.py">Location</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="./nutrition.py">Nurtition</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="./bmi.py">BMI Calculator</a>
              </li>
              <li class="nav-item">
                <a class="btn-navbar" href="#contact-us">Join Now</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <div class="container">
        <h1>Red Muscle Gym Location </h1>
        <div id="map"></div>
        <!-- Your schedule table or other content here -->
        <h2>Gym Working Hours</h2>
        <table style="color: black;">
            <tr>
                <th>Day</th>
                <th>Opening Time</th>
                <th>Closing Time</th>
            </tr>
            <tr>
                <td>Monday</td>
                <td>6:00 AM</td>
                <td>9:00 PM</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>6:00 AM</td>
                <td>9:00 PM</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>6:00 AM</td>
                <td>9:00 PM</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>6:00 AM</td>
                <td>9:00 PM</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>6:00 AM</td>
                <td>9:00 PM</td>
            </tr>
            <tr>
                <td>Saturday</td>
                <td>8:00 AM</td>
                <td>6:00 PM</td>
            </tr>
            <tr>
                <td>Sunday</td>
                <td>Closed</td>
                <td>Closed</td>
            </tr>
        </table>
    </div>
    <section class="contact-us" id="contact-us">
        <div class="container">
          <div class="row">
            <!-- Contact Info Section -->
            <div class="col-lg-6">
              <div class="contact-info">
                <h2 class="heading-contact">STAY IN TOUCH</h2>
                <p class="para-contact">
                  We are here to answer any questions you may have about our products. Reach out to us and we'll respond as soon as we can.
                </p>
                <ul class="contact-list">
                  <li><i class="fas fa-map-marker-alt"></i> Umapathi Towers - 72 Lakshmipuram, 6th Street, Masakalipalayam Rd, Peelamedu, Coimbatore, Tamil Nadu 641004</li>
                  <li><i class="fas fa-phone-alt"></i><a href="tel:+918760961525" class="num-contact"> Phone: +91 8760961525</a></li>
                  <li><i class="fas fa-envelope"></i><a href="mailto:allendarson27@gmail.com" class="num-contact"> Email: servicesector.redmusclegym@gmail.com</a></li>
                </ul>
              </div>
            </div>
 <div class="col-lg-6">
              <form class="contact-form">
                  <div class="form-group">
                      <input type="text" class="form-control" placeholder="Your Name" name="name" required>
                  </div>
                  <div class="form-group">
                      <input type="email" class="form-control" placeholder="Your Email" name="mail" required>
                  </div>
                  <div class="form-group">
                      <label for="Services" class="service">Services</label>
                      <select class="dd" id="Services" name="services" required>
                          <optgroup label="Class" class="drop">
                              <option value=""></option>
                              <option value="Strength Training">Strength Training</option>
                              <option value="Weight Loss & Weight Gain">Weight Loss & Weight Gain</option>
                              <option value="Calisthenics">Calisthenics</option>
                              <option value="Body Building">Body Building</option>
                              <option value="Powerlifting">Powerlifting</option>
                              <option value="Sports-specific Training">Sports-specific Training</option>
                              <option value="Zumba Dance Training">Zumba Dance Training</option>
                          </optgroup>
                      </select>
                  </div>
                  <div class="form-group">
                      <textarea class="form-control" rows="5" placeholder="Your Message" name="msg" required></textarea>
                  </div>
                    <input type="submit" name="submit" class="btn btn-info">
              </form>""")
import smtplib
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="gym")
cur = conn.cursor()

form = cgi.FieldStorage()

pid = form.getvalue("id")
pname = form.getvalue("name")
pemailid = form.getvalue("mail")
pservices = form.getvalue("services")
pmessage = form.getvalue("msg")
psubmit = form.getvalue("submit")

if psubmit != None:
    q = """insert into enquire(Name,Email,Services,Message) values('%s','%s','%s','%s')""" % (
    pname, pemailid, pservices, pmessage)
    cur.execute(q)
    conn.commit()

    fromaddr = "allendarson27@gmail.com"
    password = "ebbg qhms qvcr xuuk"
    toaddr = pemailid
    subject = "Hi,We Heard You"
    body = """ Username: '%s' \n mailid: '%s' \n Service: '%s' \n Yes you heard it right , We heard your request from you , and we like to assist you further and unfortunately our team is not active now , we will surely call you back """ % (
    pname, pemailid, pservices)
    msg = """ Subject:{}\n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print("""
        <script>
            alert("Thank You for your Registration");
        </script>
    """)

conn.close()
print("""</div>
      </div>
  </div>
</section>
<!--foooter-->
<footer class="footer">
  <div class="container">
      <div class="footer-content">
          <div class="footer-about">
              <h3 class="footer-logo">The Red Muscle GYM</h3>
              <p>Strength.Dedication.Power</p>
          </div>
          <ul class="footer-links">
              <li><a href="#">Home</a></li>
              <li><a href="./aboutus.py">About Us</a></li>
              <li><a href="./bmi.py">BMI Calculator</a></li>

          </ul>
          <div class="footer-social">
              <a href="https://www.facebook.com/"><i class="fab fa-facebook-f"></i></a>
              <a href="https://x.com/?lang=en"><i class="fab fa-twitter"></i></a>
              <a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a>
          </div>
      </div>
      <div class="footer-bottom">
          <p>&copy; 2024 The Red Muscle Gym. All rights reserved. 
      </div>
  </div>
</footer>
  </body>
<!-- script file -->
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</html>""")