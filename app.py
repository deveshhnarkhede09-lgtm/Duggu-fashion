from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title> Designer Clothing</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial, sans-serif;
}

body{
background:#f5f5f5;
color:#333;
}

header{
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 60px;
background:#111;
color:white;
position:sticky;
top:0;
}

.logo{
font-size:32px;
font-weight:bold;
letter-spacing:3px;
color:gold;
}

nav a{
color:white;
text-decoration:none;
margin-left:25px;
font-size:18px;
}

nav a:hover{
color:gold;
}

.hero{
height:90vh;
background:url("https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1600") center center/cover;
display:flex;
justify-content:center;
align-items:center;
text-align:center;
}

.overlay{
background:rgba(0,0,0,.55);
padding:60px;
border-radius:15px;
color:white;
}

.overlay h1{
font-size:60px;
margin-bottom:20px;
}

.overlay p{
font-size:24px;
margin-bottom:30px;
}

button{
padding:15px 40px;
font-size:18px;
background:gold;
border:none;
cursor:pointer;
border-radius:6px;
font-weight:bold;
}

button:hover{
background:#ffcc00;
}

.products{
padding:80px 40px;
text-align:center;
}

.products h2{
font-size:40px;
margin-bottom:40px;
}

.cards{
display:flex;
justify-content:center;
gap:30px;
flex-wrap:wrap;
}

.card{
background:white;
width:300px;
padding:20px;
border-radius:12px;
box-shadow:0 5px 15px rgba(0,0,0,.15);
transition:.3s;
}

.card:hover{
transform:translateY(-8px);
}

.card img{
width:100%;
height:350px;
object-fit:cover;
border-radius:10px;
}

.card h3{
margin-top:15px;
font-size:24px;
}

.card h3.clickable{
cursor:pointer;
color:#111;
text-decoration:underline;
}

.order-section{
padding:80px 40px;
background:#fff;
}

.order-section .card{
max-width:720px;
margin:auto;
box-shadow:none;
}

.order-section form{
display:flex;
flex-direction:column;
gap:15px;
text-align:left;
}

.order-section input,
.order-section textarea,
.order-section select{
width:100%;
padding:12px;
border:1px solid #ccc;
border-radius:6px;
font-size:16px;
}

.order-section button{
width:fit-content;
align-self:flex-start;
padding:15px 35px;
background:#111;
color:#fff;
border:none;
border-radius:6px;
cursor:pointer;
}

.price{
font-size:22px;
color:#c49b00;
margin-top:10px;
font-weight:bold;
}

.about{
background:white;
padding:80px;
text-align:center;
}

.about h2{
font-size:38px;
margin-bottom:20px;
}

.about p{
max-width:800px;
margin:auto;
font-size:18px;
line-height:1.8;
}

.contact{
background:white;
padding:80px;
text-align:center;
}

.contact h2{
font-size:38px;
margin-bottom:20px;
}

.contact p{
font-size:18px;
line-height:1.8;
margin:10px 0;
}

.contact a{
color:#111;
text-decoration:none;
font-weight:bold;
}

footer{
background:#111;
color:white;
text-align:center;
padding:25px;
margin-top:60px;
}

</style>

</head>

<body>

<header>

<div class="logo">DUGGU</div>

<nav>
<a href="#">Home</a>
<a href="#collection">Collection</a>

<a href="#men">Men</a>

<a href="#women">Women</a>  

<a href="#contact">Contact</a>


</nav>

</header>

<section class="hero">

<div class="overlay">

<h1>Duggu Designer Fashion</h1>

<p>Premium Clothing for Every Occasion</p>

<button onclick="alert('Shopping feature coming soon!')">
Shop Now
</button>

</div>

</section>

<section id="collection" class="products">

<h2>Featured Collection</h2>

<div class="cards">

<div class="card">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxaYEkvBfW9czJt16iPGtZx3tXQJsKRl56PVBpsfEQrZ3OpwubUNvlobs&s=10">
<h3 onclick="showOrder('Designer Jacket')" class="clickable">Designer Jacket</h3>
<p class="price">₹2,499</p>
</div>



<div class="card">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSWm83M8lfIya4BTbe-eGlxJz6lB_xuQM8h9y8fSCA0A&s=10">
<h3 onclick="showOrder('Luxury Hoodie')" class="clickable">Luxury Hoodie</h3>
<p class="price">₹1,199</p>
</div>


<div class="card">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYJY31JUgotkV2KsfxmdYrCaL2p0KYbvEdMgoMHUHpIw&s=10">
<h3 onclick="showOrder('Premium Shirt')" class="clickable">Premium Shirt</h3>
<p class="price">₹999</p>
</div>

<div class="card">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQZl34Xq_MV5o33gaiZcMn2zlDr0fiS5gR2F4aWbCXQ&s=10">
<h3 onclick="showOrder('Fashion Jeans')" class="clickable">Fashion Jeans</h3>
<p class="price">₹1,299</p>
</div>

</div>

</section>

<section id="orderSection" class="products order-section" style="display:none;">

<h2 id="orderTitle">Buy Designer Jacket</h2>

<div class="cards">

<div class="card" style="max-width:720px; width:100%;">
<form id="orderForm">
<label for="product">Product</label>
<input type="text" id="product" name="product" value="Designer Jacket" readonly>
<label for="paymentMethod">Payment Method</label>
<select id="paymentMethod" name="paymentMethod" required>
<option value="Credit Card">Credit Card</option>
<option value="UPI">UPI</option>
<option value="Net Banking">Net Banking</option>
<option value="Cash on Delivery">Cash on Delivery</option>
</select>
<label for="address">Address</label>
<textarea id="address" name="address" placeholder="Your shipping address" required></textarea>
<label for="phone">Phone Number</label>
<input type="tel" id="phone" name="phone" placeholder="+91 1234567890" required>
<button type="submit">Buy Now</button>
<p id="orderStatus" class="status"></p>
</form>
</div>

</div>

</section>

<section id="men" class="products">

<h2>Men Store</h2>

<div class="cards">

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/1_4005ac0d-b9df-4bec-acf2-6996293a66ba.jpg?v=1782409429&quality=80">
<h3 onclick='showOrder("Men's 100% Cotton Oxford Stripes Shirt")' class="clickable">Men's 100% Cotton Oxford Stripes Shirt</h3>
<p class="price">₹1,099</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/4MSR5449-05_9.jpg?v=1782296729&quality=80">
<h3 onclick='showOrder("Men's TROUSERS")' class="clickable">Men's TROUSERS</h3>
<p class="price">₹959</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/4MST2242-03-M29.jpg?v=1755866459&quality=80">
<h3 onclick='showOrder("Men's POLO SHIRT")' class="clickable">Men's POLO SHIRT</h3>
<p class="price">₹899</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/1_c1f8a875-13f8-482b-9d93-88bfb799c001.jpg?v=1783668691&quality=80">
<h3 onclick='showOrder("Men's JEANS")' class="clickable">Men's JEANS</h3>
<p class="price">₹1,149</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/4MSO4564-01_2.jpg?v=1750315500&quality=80">
<h3 onclick='showOrder("Men's CARGO PANTS")' class="clickable">Men's CARGO PANTS</h3>
<p class="price">₹959</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/1_22ceec74-6c0e-4982-93d9-aea2bbaa88d2.jpg?v=1781692777&quality=80">
<h3 onclick='showOrder("Men's T-SHIRTS")' class="clickable">Men's T-SHIRTS</h3>
<p class="price">₹1,149</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/1_0fea8cbd-4b19-4fc6-81b9-03665c8cc76d.jpg?v=1778087283&quality=80">
<h3 onclick='showOrder("Men's SHORTS")' class="clickable">Men's SHORTS</h3>
<p class="price">₹1,129</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/1_6ab057c8-d132-4379-bda7-5478d22577eb.jpg?v=1780407502&quality=80">
<h3 onclick='showOrder("Men's PLUS SIZE")' class="clickable">Men's PLUS SIZE</h3>
<p class="price">₹1,799</p>
</div>

<div class="card">
<img src="https://cdn.shopify.com/s/files/1/0420/7073/7058/files/2_1bba09f6-66c2-4c3b-a17e-6e084b6d2937.jpg?v=1778658551&quality=80">
<h3 onclick='showOrder("Men's SHOES")' class="clickable">Men's SHOES</h3>
<p class="price">₹2,499</p>
</div>


</div>

</section>

<section id="women" class="products">

<h2>Women Store</h2>

<div class="cards">

<div class="card">
<img src="https://m.media-amazon.com/images/I/71xwc0+YreL._SY879_.jpg">
<h3 onclick='showOrder("Women's Formal")' class="clickable">Women's Formal</h3>
<p class="price">₹1,499</p>
</div>

<div class="card">
<img src="https://m.media-amazon.com/images/I/51jOoX3aoQL._SY879_.jpg">
<h3 onclick='showOrder("Women's office wear")' class="clickable">Women's office wear</h3>
<p class="price">₹2,299</p>
</div>

<div class="card">
<img src="https://m.media-amazon.com/images/I/51JtGs04X7L._SY741_.jpg">
<h3 onclick='showOrder("Women's Kurta")' class="clickable">Women's Kurta</h3>
<p class="price">₹999</p>
</div>

<div class="card">
<img src="https://m.media-amazon.com/images/I/61a770ncRFL._SY879_.jpg">
<h3 onclick='showOrder("Women's tops")' class="clickable">Women's tops</h3>
<p class="price">₹489</p>
</div>

</div>

</section>

<section class="about">

<h2>About DUGGU</h2>

<p>
DUGGU is a premium designer clothing brand focused on timeless elegance,
high-quality craftsmanship, and modern fashion. Explore exclusive collections
crafted for style, comfort, and confidence.
</p>

</section>

<section id="contact" class="contact">
<h2>Contact Us</h2>
<p>For inquiries, reach out to our fashion store:</p>
<p>Email: <a href="mailto:duggu.contact@gmail.com">duggu.contact@gmail.com</a></p>
<p>Phone: <a href="tel:+91 755****93">+91 755****93</a></p>
<p>Address: 1st floor New Cbs Opposite Bali Mandri, Nashik, India</p>
</section>

<button id="openFeedbackBtn" style="background-color: #111; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
Give your feedback
</button>

<!-- Feedback slide panel -->
<div id="feedbackPanel" class="feedback-panel">
    <div class="feedback-header">
        <h3>Send Feedback</h3>
        <button id="closeFeedbackBtn">✕</button>
    </div>
    <form id="feedbackForm">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your name" />
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="you@example.com" />
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Your feedback" required></textarea>
        <button type="submit" class="submit-btn">Submit</button>
    </form>
    <p id="feedbackStatus" class="status"></p>
</div>

<style>
.feedback-panel { position: fixed; right: -420px; top: 60px; width: 380px; max-width: 90%; height: auto; background: #fff; box-shadow: 0 8px 24px rgba(0,0,0,0.2); border-radius: 8px; padding: 16px; transition: right 0.3s ease; z-index: 9999; }
.feedback-panel.open { right: 20px; }
.feedback-header { display:flex; justify-content:space-between; align-items:center; }
.feedback-header h3 { margin:0; }
.feedback-header button { background:transparent; border:none; font-size:18px; cursor:pointer; }
.feedback-panel label { display:block; margin-top:10px; font-size:14px; }
.feedback-panel input, .feedback-panel textarea { width:100%; padding:8px; margin-top:6px; box-sizing:border-box; border:1px solid #ccc; border-radius:4px; }
.feedback-panel .submit-btn { margin-top:10px; background:#111; color:#fff; border:none; padding:10px; border-radius:4px; cursor:pointer; }
.feedback-panel .status { margin-top:8px; font-size:14px; }
</style>

<script>
document.getElementById('openFeedbackBtn').addEventListener('click', function(){
    document.getElementById('feedbackPanel').classList.add('open');
});
document.getElementById('closeFeedbackBtn').addEventListener('click', function(){
    document.getElementById('feedbackPanel').classList.remove('open');
});
document.getElementById('feedbackForm').addEventListener('submit', async function(e){
    e.preventDefault();
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };
    const status = document.getElementById('feedbackStatus');
    status.textContent = 'Sending...';
    try{
        const res = await fetch('/feedback', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data) });
        const json = await res.json();
        if(res.ok) { status.textContent = json.message || 'Thank you for your feedback!'; document.getElementById('feedbackForm').reset(); }
        else status.textContent = json.error || 'Failed to send feedback.';
    } catch(err){ status.textContent = 'Network error.'; }
});

document.getElementById('orderForm').addEventListener('submit', async function(e){
    e.preventDefault();
    const orderData = {
        product: document.getElementById('product').value,
        paymentMethod: document.getElementById('paymentMethod').value,
        address: document.getElementById('address').value,
        phone: document.getElementById('phone').value
    };
    const statusEl = document.getElementById('orderStatus');
    statusEl.textContent = 'Processing order...';
    try{
        const res = await fetch('/order', {
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify(orderData)
        });
        const json = await res.json();
        if(res.ok){
            statusEl.textContent = json.message || 'Order received!';
            console.log('Order sent:', orderData);
        } else {
            statusEl.textContent = json.error || 'Failed to place order.';
        }
    } catch(err){
        statusEl.textContent = 'Network error.';
    }
});

function showOrder(product){
    document.getElementById('orderSection').style.display = 'block';
    document.getElementById('product').value = product;
    document.getElementById('orderTitle').textContent = 'Buy ' + product;
    document.getElementById('orderStatus').textContent = '';
    document.getElementById('address').focus();
}
</script>

<footer>

<h3>DUGGU    Designer Clothing</h3>
<p>© 2026 All Rights Reserved.</p>

</footer>

</body>

</html>
"""

@app.route("/")
def home():
    return render_template_string(html)





from flask import request, jsonify


@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json() or {}
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    # For now just print to console; in real app save to DB or send email
    print('Feedback received:', name, email, message)
    return jsonify({'message':'Feedback received'}), 200


@app.route('/order', methods=['POST'])
def order():
    data = request.get_json() or {}
    product = data.get('product', '')
    payment_method = data.get('paymentMethod', '')
    address = data.get('address', '')
    phone = data.get('phone', '')
    print(f'Order received: {product} | Payment method: {payment_method} | Address: {address} | Phone: {phone}')
    return jsonify({'message':'Order received. Thank you!'}), 200


if __name__ == "__main__":
    app.run(debug=True)