#!C:/Users/USER/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src='https://kit.fontawesome.com/4c729db828.js' crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js" integrity="sha512-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="media.css">
    <style>
      .num-contact{
            text-decoration: none;
            color: #a7a7a7;
        }
    </style>
    <title>RED MUSCLE GYM</title>
  </head>
<body>
    <div class="header">
        <div class="container-fluid gx-0">
            <!--navbar start--> 
            <nav class="navbar navbar-expand-lg">
                <div class="container">
                  <a class="navbar-brand logo text-uppercase" href="./index.py">The Red Muscle Gym</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                      <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="index.py">Home</a>
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
            <!--navbar end-->
            <div class="container">
              <div class="content-home">
                  <div class="row content-home2">
                      <div class="col-lg-7 col-md-5">
                          <div class="box-container">
                              <img src="./run-4181899_1920.png" class="img-home" alt="banner img">
                          </div>
                      </div>
                      <div class="col-lg-5 col-md-7">
                          <div class="box-container2">
                              <h1 class="home-heading"><span class="home-span">Weight Loss & Gain</span></h1>
                              </div>
                      </div>    
                  </div>
              </div>
          </div>

          
        <div class = "col-lg-12">
        <div class="container" id="aboutus">
          <div class="loss gain">
              <div class="weight-us">
                  <div class="row">
                      <div class="col-lg-6">
                          <div class="content-about">
                              <h2 class="heading-about">Weightloss</h2>
                              <p class="para-about">
                                  Weight loss involves reducing body weight through a combination of healthy eating, regular physical activity, and lifestyle changes. It focuses on creating a calorie deficit, where calories burned exceed calories consumed. Effective weight loss strategies include a balanced diet rich in whole foods, lean proteins, fruits, and vegetables, along with regular exercise such as cardio, strength training, and flexibility workouts. Adequate sleep, hydration, and stress management are also crucial. Sustainable weight loss emphasizes gradual, consistent progress rather than quick fixes, promoting long-term health benefits and reducing the risk of chronic diseases like diabetes, heart disease, and obesity..
                              </p> 
                          </div>
                      </div>
                      <div class="col-lg-6">
                        <h2 class="heading-about">Benifits</h2>
                        <p class="para-about">
                            Weight loss offers a multitude of health benefits, enhancing both physical and mental well-being. One of the primary advantages is the reduction in the risk of chronic diseases. Losing weight helps lower the likelihood of developing conditions such as heart disease, type 2 diabetes, high blood pressure, and certain types of cancer. Improved cardiovascular health is a significant benefit, as weight loss can lead to better cholesterol levels and lower blood pressure, reducing the strain on the heart..  
                        </p> 
                        <p class="para-about">
                            Additionally, weight loss improves metabolic health. It enhances insulin sensitivity, which is crucial for preventing diabetes and managing blood sugar levels. Joint health also benefits significantly, as reduced body weight decreases the pressure on joints, alleviating symptoms of arthritis and improving mobility and flexibility..
                        </p>
                        <p class="para-about">
                            Mental health improvements are another vital aspect. Weight loss can boost self-esteem and confidence, reducing symptoms of depression and anxiety. It often leads to better sleep quality and increased energy levels, making daily activities more manageable and enjoyable.
                        </p>
                      </div>
                  </div>
              </div>
          </div>
        </div>
<div class="col-md-12">
</div>   
          <div class="container" id="aboutus">
              <div class="loss gain">
                  <div class="weight-us">
                      <div class="row">
                          <div class="col-lg-6">
                              <div class="content-about">
                                  <h2 class="heading-about">Weightgain</h2>
                                  <p class="para-about">
                                      Weight gain involves increasing body weight through a combination of dietary adjustments, strength training, and lifestyle changes. It often focuses on gaining muscle mass rather than fat. Effective strategies include consuming calorie-dense, nutrient-rich foods such as lean proteins, whole grains, healthy fats, and vegetables. Regular strength training exercises are essential to build and maintain muscle. Adequate sleep and stress management also play crucial roles. Weight gain can be beneficial for individuals underweight or those seeking to enhance their athletic performance. It improves energy levels, physical strength, and overall health when approached in a balanced and healthy manner.
                                  </p> 
                                  
                              </div>
                          </div>
                          <div class="col-lg-6">
                            <h2 class="heading-about">Benifits</h2>
                            <p class="para-about">
                                Weight gain, when achieved in a healthy and controlled manner, offers several benefits for individuals looking to increase muscle mass and overall body weight. Firstly, it helps improve physical strength and endurance. Increased muscle mass enhances the body's ability to perform physical activities and tasks, from everyday movements to athletic endeavors.  
                            </p> 
                            <p class="para-about">
                                Furthermore, weight gain can lead to improved metabolic health. Adequate calorie intake supports optimal energy levels and metabolic function, aiding in better digestion and nutrient absorption. This can contribute to overall vitality and well-being.
                            </p>
                            <p class="para-about">
                                Weight gain also plays a crucial role in enhancing immune function. Proper nutrition and a balanced diet rich in vitamins, minerals, and proteins support immune system strength, reducing the risk of infections and promoting faster recovery from illness or injury.Additionally, achieving a healthy weight can boost self-confidence and self-esteem. For individuals who were underweight or struggling with body image, reaching a healthier weight can lead to improved mental well-being and a more positive self-perception..
                            </p>
                          </div>
                      </div>
                  </div>
              </div>
            </div>
  <!--TESTIMONIALS-->
  <div style="margin-top: 220px;"></div>
<section class="testimonial">
  <h2 class="heading-testimonial">
  What Our Customers Think <span class="styling">About Us</span>
  </h2>
<p class="para-testimonial">At Red Muscle Unisex Fitness Center, we take pride in the positive feedback and testimonials we receive from our valued members. Here's what some of our customers have to say about their experience with us:</p>
<div class="container-fluid">
  <div id="carouselExampleIndicators" class="carousel slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    </div>
    <div class="carousel-inner">
      <!-- Slide 1 -->
      <div class="carousel-item active">
        <div class="container container-clients">
          <div class="row">
            <div class="col-lg-4 col-md-6 my-2">
              <div class="container-content">
                <div class="img-client"></div>
                <div class="star">
                  <ul class="rating">
                    <li class="stars"><i class="fa-solid fa-star"></i></li>
                    <li class="stars"><i class="fa-solid fa-star"></i></li>
                    <li class="stars"><i class="fa-solid fa-star"></i></li>
                    <li class="stars"><i class="fa-solid fa-star"></i></li>
                    <li class="stars"><i class="fa-solid fa-star"></i></li>
                  </ul>
                  <h3 class="client-name">Karthibakrishnan</h3>
                  <p class="para-client">"Red Muscle has transformed my fitness journey. The facilities are top-notch, and the trainers are incredibly supportive. I've never felt more motivated to reach my goals."<p>
                      <h5 class="profession">Calishenics</h5>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 my-2">
            <div class="container-content">
              <div class="img-client"></div>
              <div class="star">
                <ul class="rating">
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                </ul>
                <h3 class="client-name">Aadhityan</h3>
                <p class="para-client">"A gym with good ambience. Staffs are very friendly and giving good support for all clients. General training is very good especially my trainer Robin is supporting very well. Thank you so much"</p>
                <h5 class="profession">Bodybuilding</h5>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 my-2">
            <div class="container-content">
              <div class="img-client"></div>
              <div class="star">
                <ul class="rating">
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                </ul>
                <h3 class="client-name">sakthivel</h3>
                <p class="para-client">"Neat and clean gym spacious and hygienic. Very comfortable for women. Highly recommended. Trainers are helpful and friendly in nature."</p>
                <h5 class="profession">Weightloss</h5>  
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Slide 2 -->
    <div class="carousel-item">
      <div class="container container-clients">
        <div class="row">
          <div class="col-lg-4 col-md-6 my-2">
            <div class="container-content">
              <div class="img-client"></div>
              <div class="star">
                <ul class="rating">
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                  <li class="stars"><i class="fa-solid fa-star"></i></li>
                </ul>
                <h3 class="client-name">Vignesh</h3>
                <p class="para-client">"Gym ambience is very good and neatly maintained traines are well knowledge it’s one of the peaceful place to workout without distractions."</p>
                <h5 class="profession">Weightloss</h5>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 my-2">
              <div class="container-content">
                  <div class="img-client"></div>
                  <div class="star">
                    <ul class="rating">
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                    </ul>
                    <h3 class="client-name">joshep</h3>
                    <p class="para-client">"I have been a member for 1 year I have seen a big amount of difference. They have very good trainers who guided me very well"</p>
                    <h5 class="profession">Bodybuilding</h5>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 my-2">
                <div class="container-content">
                  <div class="img-client"></div>
                  <div class="star">
                    <ul class="rating">
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                      <li class="stars"><i class="fa-solid fa-star"></i></li>
                    </ul>
                    <h3 class="client-name">sanjay</h3>
                    <p class="para-client">"Wonderful gym, great environment for workouts. The trainers are encouraging, supportive and knowledgeable. Awesome place to start our fitness journeys."</p>
                    <h5 class="profession">Weight gain</h5>
                  </div>
                </div>
              </div>
          </div>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</div>
</div>
<!--contact us page-->
<!-- Contact Us Section -->
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