# Testing

* When building this site, I would test at every step of progress. Each function that was added in a view needed to be tested immediately before proceeding on with any additional functionality or coding. If anything went wrong, I would debug and find a solution before moving on.

### Python Validation - Pycodestyle
* I had an issue with my IDE linter. So all code was written manually which was great practice. When I ran Python Validation I had a lot of errors to fix but it was worth it. All Python files were reviews.

## Python Files Reviews

#### Main App / Project Root - Drum Loot

* asgi.py
* urls.py
* views.py
* wsgi.py
* settings.py

#### App - Cart

* apps.py
* context.py
* urls.py

#### App - Checkout

* admin.py
* apps.py
* forms.py
* models.py
* signals.py
* urls.py
* views.py
* webhook_handler.py
* webhooks.py

#### App - Home / Contact

* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py

#### App - Products

* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py
* widgets.py

#### App - Profiles

* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py

#### App - Reviews

* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py
* widgets.py

### PEP8 Compliant

All Python code written by me passes PEP8 standards [CI Python Linter](https://pep8ci.herokuapp.com/).

### HTML WC3 Validator

All HTML Code written by me passed through the [WC3 HTML validator](https://validator.w3.org/#validate_by_url).
- All issues were resolved.

### Jigsaw CSS Validator

All CSS Code Passed Validation 

### Lighthouse Validation

- Lighthouse testing did well for accessibility to SEO. However there is room for improvement on images. Even though I resized each image individually, the load time on images seems to be low.

## Manual Testing

## Manual Testing

|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Register     |                        |                  |      |             |
| 1           | Click on the register button | Redirected to register page | Y |          |
| 2           | Click on Sign Up | User is logged in and receives a message | Y |          |
| 3           | Enter valid email | Field will only accept email address format | Y |          |
| 4           | Enter valid username | Username must be unique | Y |          |
| 5         | Enter valid password | Field will only accept secure passwords | Y |          |
| 6          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 7          | Click the sign in link| Takes user to the sign in page | Y |          |
| My Account      |                        |                  |      |             |
| 1           | Click on My Account button in the navbar | Drop down options appear | Y |          |
| 1           | Click on Login button in the navbar | Brought to login page | Y |          |
| 2           | Click on the Register link in the form | Redirected to the sign up page | Y |          |
| 3           | Enter valid password | Field will only accept correct passwords | Y |          |
| 4           | Click on the Sign In button | Takes user to the index page abd receives confirmation message | Y |          |
| 5           | Click "Logout" in the navbar | Takes user to log out page to confirm logout | Y |          |
| 6           | Click "Logout" button on the page | Redirects user to index page and receive confirmation message | Y |          |
| 2           | Click "Product Management" in the navbar | Brings user to page if superuser | Y | Upon adding the product it is added to the database  |
| 4           | Click "Register" in the navbar | Brings user to sign up page | Y |          |
| 4           | Click "My Profile" in the navbar | Brings user to the profile page | Y |          |
| Navigation     |                        |                  |      |             |
| 1          | Click "Logo" in the navbar | Brings user to Home page | Y |          |
| 6          | Click the "Filter Products by" link and all menu items | Takes user to the products page with the correct products filtered | Y |          |
| 6          | Click the "Home Decoration" link and all menu items | Takes user to the products page with the correct products filtered | Y |          |
| 6          | Click the "For Children" link and all menu items | Takes user to the products page with the correct products filtered | Y |          |
| 6          | Click the "Antique" link and all menu items | Takes user to the products page with the correct products filtered | Y |          |
| 6          | Click the "Contact us" link | Takes user to the contact us page | Y |          |
| Homepage  |                        |                  |      |             |
| 1      | Click on shop now button | Redirects user to the products page | Y |          |
| Products Page  |                        |                  |      |             |
| 1        | Click on product image | Brings user to product detail page | Y |          |
| 2        | Click on the add to favorites button | User receives message saying thank you and favorite added to database | Y |          |
| 4  | Click on the delete button as superuser  | Product is deleted | Y |          |
| 5  | Click on the edit button  | User is redirected to the edit product page | Y |  Upon editing the comment the product is updated        |
| 8  | Visit the delete product url while not signed in as that user  | User is redirected to a page saying you can only modify products if you are an admin them | Y |          |
| 9  | Visit the edit product url while not signed in as that user  | User is redirected to a page saying you can only modify products if you are an admin | Y |          |
| Admin Panel  |                        |                  |      |             |
| 1    | Open admin url while signed in as a regular user | User is informed they are not authorized and is prompted to sign in with a different account  | Y |          |
| 2    | Sign in as the superuser | Redirects user to the admin panel | Y |          |
| 3   | Click on any of the models in the admin panel | User sees a list of the objects with that model | Y |     |
| 4    | Click a specific object within the list of models  | User is shown the properties of that object | Y |  The user may modify, delete, or add objects from this page    |
| 5     | Click delete on an object | User is taken to delete confirmation page and upon confirmation receive a message at the top of the page | Y |   |
| 6     | Approve a user comment | The comment shows as approved and all users can then view that comment | Y |    |
| 7         | Unapprove a user comment | The comment can only be seen by the admin until the comment is approved | Y |          |
| 8       | Edit a post | The content of the post reflects the changes made | Y |          |
| 404 Page  |                        |                  |      |             |
| 9        | Enter an invalid url  | User redirected to a custom 404 error page | Y |          |
| Payments  |                        |                  |      |             |
| 1    | Click secure checkout  | Y | User is taken to checkout page and order summary is shown | Y |          |
| 2    | Fill in information and submit form | Order is processed and user taken to success page | Y |  All form validation functions correctly        |
| 3   | Remove or change contents in the cart | The user can change quantity or remove products as wanted | Y |     |
| 4    | Click a specific object within the list of models  | User is shown the properties of that object | Y |  The user may modify, delete, or add objects from this page    |


## Bugs

- I had an issue with Heroku deployment. My Database did not migrate correctly. Luckily I still had all of my products and reviews on my local. So I researched how to loaddata onto a JSON file in order to migrate them across to my DB.

- I created the ability to do a sale on an item. I updated the product and product detail template. While the discounted price was showing, I then realised that the cart was not reflecting the same prices. I quickly dived into the cart code to add in the sale pricing logic.

- I had issues with template includes. I refactored the code in my cart but when I went to test this, I got an error straight away to tell me that product-images.html template I created did not exist. I knew it did exist. When I checked the include, it was set correctly. I dealt with Tutot support and we still couldn't find it. I realised then it was the second include URL that was causing the entire page to throw the error. I was wondering why it never had an issue with my cart-total.html include, since that would be rendered first if I had issues in my settings.py file, this would be a problem too. I then found the second URL and realised it was missing cart/ - {% include 'product-images.html' %} vs {% include 'cart/product-images.html' %}. Such as small issue can cause such a big problem!




