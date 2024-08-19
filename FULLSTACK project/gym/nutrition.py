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
                              <img src="./img/ai-generated-8619138.png" class="img-home" alt="banner img">
                          </div>
                      </div>
                      <div class="col-lg-5 col-md-7">
                          <div class="box-container2">
                              <h1 class="home-heading"><span class="home-span">Nutritions</span></h1>
                              </div>
                      </div>    
                  </div>
              </div>
          </div>

          <div class="container" id="aboutus">
            <div class="Nutrition">
                <div class="health-us">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="content-about" style="background-color: transparent;">
                                <h2 class="heading-about">NUTRITIONS</h2>
                                <p >
                                  Proper nutrition is essential for maximizing performance, building muscle, and supporting recovery when engaging in gym training. A balanced diet that includes the right proportions of macronutrients, micronutrients, and hydration is key to achieving fitness goals.
                                    </p> 
                                <h2 class="heading-about">Macronutrients</h2>
                                <p >
                                    1.Protein:Essential for muscle repair and growth.Recommended intake: 1.6-2.2 grams per kilogram of body weight.Sources: lean meats, poultry, fish, eggs, dairy, legumes, and plant-based proteins (e.g., tofu, tempeh).<br>
                                    2.Carbohydrates:Primary energy source for high-intensity workouts.Recommended intake: 3-5 grams per kilogram of body weight for moderate activity, 6-10 grams for high-intensity training.Sources: whole grains, fruits, vegetables, legumes, and starchy foods (e.g., potatoes, rice).
                                    <br>
                                    3.Fats:Supports hormone production and provides long-lasting energy.Recommended intake: 0.5-1 gram per kilogram of body weight.Sources: avocados, nuts, seeds, olive oil, fatty fish, and nut butters.<br>
                                <h2 class="heading-about">Micronutrients</h2>    
                                    1.Vitamins:Essential for energy production, immune function, and overall health.Important vitamins for gym-goers: Vitamin D (bone health), B Vitamins (energy metabolism), Vitamin C (antioxidant).Sources: fruits, vegetables, whole grains, and fortified foods.<br>
                                    2.Minerals:Crucial for muscle function, bone health, and hydration.Important minerals: Calcium (bone health), Magnesium (muscle function), Iron (oxygen transport).Sources: dairy products, leafy greens, nuts, seeds, and lean meats.</p><br>
                                    <h2 class="heading-about">Pre-Workout Nutrition</h2>   
                                <p>
                                  <p>
                                    1.Timing:Eat 2-3 hours before a workout for optimal energy.If closer to workout time, consume a smaller, easily digestible snack 30-60 minutes prior.
                                    <br>
                                    2.Composition:Focus on carbohydrates and moderate protein.Example meal: chicken with brown rice and vegetables.Example snack: banana with peanut butter.
                                    <br>
                                  </p>
                                    <h2 class="heading-about">Post-Workout Nutrition</h2>
                                    <p>
                                    1.Timing:Consume a meal or snack within 30-60 minutes post-workout for recovery. This period is known as the "anabolic window."
                                    <br>
                                    2.Composition:Emphasize protein and carbohydrates to replenish glycogen stores and repair muscles.Example meal: grilled salmon with quinoa and a mixed green salad.Example snack: protein shake with a piece of fruit.
                                    <br>
                                    </p>
                                    <h2 class="heading-about">Hydration</h2>
                                    <p>
                                    1.Importance:Critical for maintaining performance and recovery.Dehydration can impair muscle function and endurance. <br>
                                    2.Guidelines:Drink water throughout the day, aiming for at least 8 cups (2 liters).Increase intake based on activity level and sweat loss.<br>
                                    </p>
                                    <h2 class="heading-about">Special Consideration</h2>
                                    <p>
                                    1.Vegetarian/Vegan Diets:Focus on plant-based protein sources like legumes, nuts, seeds, and soy products.Ensure adequate intake of Vitamin B12, Iron, and Omega-3 fatty acids through fortified foods or supplements.
                                    <br>
                                    2.Weight Management:For weight loss: Maintain a calorie deficit while ensuring adequate protein intake to preserve muscle mass.For weight gain: Increase calorie intake with nutrient-dense foods and focus on strength training.
                                    <br>
                                    </p>
                            </div>
                        </div>
                    </div>
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