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
                        <a class="nav-link" aria-current="page" href="#">Home</a>
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
                              <img src="./img/5.png" class="img-home" alt="banner img">
                          </div>
                      </div>
                      <div class="col-lg-5 col-md-7">
                          <div class="box-container2">
                              <h1 class="home-heading">Where pain meets progress, strength is <span class="home-span">born</span></h1>
                              <p class="para-home">
                                Experience the strength that lies within. Embrace the challenge, transform your limits. With each lift, write your story of growth. In every rep, find resilience and power. Experience the journey, conquer the extraordinary
                              </p>
                              <div class="btn-home">
                                  <a href="#product" class="home-links btn-2">EXPLORE</a>
                              </div>
                          </div>
                      </div>    
                  </div>
              </div>
          </div>
          <!-- About Us -->
          <div class="container" id="aboutus">
              <div class="about-us-container">
                  <div class="about-us">
                      <div class="row">
                          <div class="col-lg-6">
                              <div class="content-about">
                                  <h2 class="heading-about"> Welcome to <span class="home-span">RED MUSCLE </span></h2>
                                   <p class="para-about">
                                    At Red Muscle, we believe in creating a fitness environment that is welcoming, inclusive, and effective for everyone. Whether you're a fitness enthusiast or just starting your journey, our state-of-the-art facilities and expert trainers are here to support you every step of the way.</p>
                                  <p class="para-about">Our mission is to empower individuals to achieve their fitness goals through personalized training, cutting-edge equipment, and a supportive community. We strive to promote health, wellness, and a balanced lifestyle for all our members.
                                  </p>        
                              </div>
                          </div>
                          <div class="col-lg-6">
                            
                              <iframe width="600"  class="img-about"  height="315" src="https://www.youtube.com/embed/WlYTV0HYbNU?si=cMKwtw2z5axM-qAH" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                           
                          </div>
                         
                      </div>
                  </div>
              </div>
          </div>
          
    <!--aboutus end-->
   <!-- Carousel content here -->
      <section class="product-category" id="product">
        <h2 class="heading-product">Trainings We Provide</h2>
        <div class="container-fluid">
          <!--slider carousel botstrap-->
          <div id="carouselExample" class="carousel slide">
            <div class="carousel-inner">
              <div class="carousel-item active">
               <div class="container">
                <div class="row">
                  <div class="col-lg-4 col-md-6">
                    <div class="card card-product" >
                      <img src="./silhouette-3839252_1920.png" class="card-img-top img-card" alt="...">
                      <div class="card-body">
                       <a href="./calisthenics.py" class="product-link"> <h5 class="card-title">Calisthenics</h5> </a>
                        <p class="card-text" >Calisthenics is a form of physical exercise consisting of a variety of movements that rely on an individual's body weight, often performed with minimal equipment. This form of training focuses on building strength, flexibility, and endurance through exercises like push-ups, pull-ups, squats, and planks. It promotes functional fitness, enhancing one's ability to perform everyday activities with ease and efficiency. Calisthenics is accessible to people of all fitness levels and can be performed anywhere, making it a versatile and popular choice for many fitness enthusiasts.</p>

                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6">
                    <div class="card card-product" >
                      <img src="run-4181899_1920.png" class="card-img-top img-card" alt="...">
                      <div class="card-body">
                       <a href="./weight.py"> <h5 class="card-title">Weight Loss & Weight Gain</h5></a>
                        <p class="card-text">Weight loss and weight gain depend on the balance between calorie intake and energy expenditure. Weight loss involves consuming fewer calories than burned, achieved through a balanced diet and regular exercise, focusing on fat reduction and muscle preservation. Weight gain requires a calorie surplus, combining strength training with a nutrient-rich diet high in protein, healthy fats, and complex carbohydrates. Both require sustainable lifestyle changes, emphasizing healthy eating and consistent exercise for overall fitness.</p>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6">
                   <div class="card card-product" >
                      <img src="weightlifter-3944725_1920.png" class="card-img-top img-card" alt="...">
                      <div class="card-body">
                       <a href="./powerlifting.py"> <h5 class="card-title">Powerlifting
                        </h5> </a>
                        <p class="card-text" >Powerlifting is a strength sport that focuses on three main lifts: the squat, bench press, and deadlift. Athletes aim to lift the maximum weight possible in each of these exercises, typically competing in weight classes. The sport emphasizes raw strength and technique, with competitors performing three attempts for each lift, and the highest successful attempt for each lift is totaled to determine the winner. Powerlifting promotes overall muscle development, functional strength, and disciplined training regimens.</p>
                      </div>
                    </div>
                  </div>
                </div>
               </div>
              </div>
              <div class="carousel-item">
                <div class="container">
                  <div class="row">
                    <div class="col-lg-4 col-md-6">  
                      <div class="card card-product" >
                        <img src="bodybuilder-4743091_1920.png" class="card-img-top img-card" alt="...">
                        <div class="card-body">
                        <a href="./bodybuilding.py">  <h5 class="card-title">Bodybuilding</h5> </a>
                          <p class="card-text" >Bodybuilding is a sport and lifestyle focused on developing muscle mass, symmetry, and definition through resistance training and nutrition. Athletes engage in rigorous weightlifting routines targeting specific muscle groups to achieve a sculpted and balanced physique. Diet plays a crucial role, often involving high protein intake and precise macronutrient management to support muscle growth and fat loss. Competitors showcase their physiques in competitions, where they are judged on muscle size, proportion, and overall aesthetics. Bodybuilding emphasizes dedication, discipline, and a holistic approach to fitness and health.</p>

                        </div>
                      </div>
                      </div>  
                    <div class="col-lg-4 col-md-6">
                      <div class="card card-product" >
                        <img src="./man-2754215_1920.png" class="card-img-top img-card" alt="...">
                        <div class="card-body">
                        <a href="./sports-specific.py">  <h5 class="card-title">Sport-Specific Training</h5> </a>
                          <p class="card-text">Sports-specific training is a tailored approach to fitness that focuses on improving the skills, strength, and conditioning required for a particular sport. This type of training involves exercises and drills that mimic the movements and demands of the sport, enhancing performance, agility, and injury prevention. Athletes engage in customized workouts that address their individual needs and the physical requirements of their sport, from endurance and speed to power and flexibility. Sports-specific training helps athletes achieve peak performance and excel in their chosen sport by optimizing their physical capabilities and technical skills.</p>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6">  
                      <div class="card card-product" >
                        <img src="./carefree-1299639_1920.png" class="card-img-top img-card" alt="...">
                        <div class="card-body">
                          <a href="./zumba.py"> <h5 class="card-title">Zumba Dance Training</h5> </a>
                          <p class="card-text" >Zumba is a popular fitness program that combines dance and aerobic movements set to energetic music, creating a fun and engaging workout. Originating from Latin dance styles such as salsa, merengue, and reggaeton, Zumba routines incorporate rhythms and movements to provide both cardiovascular and strength training benefits. Suitable for people of all fitness levels, Zumba classes offer a lively and social environment, making exercise enjoyable and accessible. Participants often experience improved coordination, increased energy levels, and enhanced overall fitness while dancing to the beat.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                 </div>
              </div>
            </div>
            <button class="carousel-control-prev btn-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
             <span>
                 <i class="fa-solid fa-arrow-left btn-scrool button-left"></i>
             </span>
            </button>
            <button class="carousel-control-next btn-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
              <span>
                <i class="fa-solid fa-arrow-right btn-scrool button-right"></i>
              </span>
            </button>
          </div>
        </div>
      </section>
  
    
<!--PRODUCT PART-->
<!--TESTIMONIALS-->

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
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="gym")
cur=conn.cursor()

form=cgi.FieldStorage()

pid=form.getvalue("id")
pname=form.getvalue("name")
pemailid=form.getvalue("mail")
pservices=form.getvalue("services")
pmessage=form.getvalue("msg")
psubmit=form.getvalue("submit")

if psubmit!=None:
    q = """insert into enquire(Name,Email,Services,Message) values('%s','%s','%s','%s')""" %(pname,pemailid,pservices,pmessage)
    cur.execute(q)
    conn.commit()

    fromaddr="allendarson27@gmail.com"
    password="ebbg qhms qvcr xuuk"
    toaddr=pemailid
    subject="Hi,We Heard You"
    body = """ Username: '%s' \n mailid: '%s' \n Service: '%s' \n Yes you heard it right , We heard your request from you , and we like to assist you further and unfortunately our team is not active now , we will surely call you back """ % (
        pname, pemailid, pservices)
    msg = """ Subject:{}\n\n{}""".format(subject, body)
    server=smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromaddr,password)
    server.sendmail(fromaddr,toaddr,msg)
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