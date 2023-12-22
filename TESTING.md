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
- Some issues were not resolved.
- Any issues remaining I'm fully aware of and the website functions correctly regardless of these known issues.
- Empty heading on H1 class due to loading spinner
- Placeholder attribute for the profile form / Country field.


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
| 2           | Click on Login button in the navbar | Brought to login page | Y |          |
| 3           | Click on the Register link in the form | Redirected to the sign up page | Y |          |
| 4           | Enter valid password | Field will only accept correct passwords | Y |          |
| 5           | Click on the Sign In button | Takes user to the index page and receives confirmation message | Y |          |
| 6           | Click "Logout" in the navbar | Takes user to log out page to confirm logout | Y |          |
| 7           | Click "Logout" button on the page | Redirects user to index page and receive confirmation message | Y |          |
| 8           | Click "Product Management" in the navbar | Brings user to page if superuser | Y | Upon adding the product it is added to the database  |
| 9           | Click "Register" in the navbar | Brings user to sign up page | Y |          |
| 10           | Click "My Profile" in the navbar | Brings user to the profile page | Y |          |
| 11          | Click "Forgot My Password" on login page| Redirects user to forgot password page | Y |          |
| Navigation     |                        |                  |      |             |
| 1          | Click "Logo" in the navbar | Brings user to Home page | Y |          |
| 2          | Click the "All Products" link | Dropdown menu appears | Y |          |
| 3          | Click the "Acoustic Drums" link | Dropdown menu appears | Y |          |
| 4          | Click the "Electric Drums" link | Dropdown menu appears | Y |          |
| 5          | Click the "Special Offers" link | Dropdown menu appears | Y |          |
| 6          | Click the "Contact Reviews" link | Dropdown menu appears | Y |          |
| 7          | Click on each "All Products" menu items | Brings User to appropriate filtered page | Y |          |
| 8          | Click on each "Acoustic Drums" menu items | Brings User to appropriate filtered page | Y |          |
| 9          | Click on each "Electric Drums" menu items | Brings User to appropriate filtered page | Y |          |
| 10          | Click on each "Special Offers" menu items | Brings User to appropriate filtered page | Y |          |
| 11         | Click on each "Contact Reviews" menu items | Brings User to appropriate filtered page | Y |          |
| Search    |                        |                  |      |             |
| 1      | Enter a search term into the box provided and click search | Redirects users to filtered search results | Y |          |
| Homepage  |                        |                  |      |             |
| 1      | Click on Special Offers button over hero image | Redirects user to the Special Offers page | Y |          |
| Products Page  |                        |                  |      |             |
| 1        | Click on product image | Brings user to product detail page | Y |          |
| 2        | Click on "+" or "-" to adjust quantity | Number changes to reflect interaction | Y |          |
| 3        | Click on "Add to Cart"  button | Adds product to shopping cart with appropriate quantity | Y |          |
| 4  | Click on the delete button as superuser  | Product is deleted | Y |          |
| 5  | Click on the edit button  | User is redirected to the edit product page | Y |  Upon editing the comment the product is updated        |
| 6  | Visit the delete product url while not signed in as that user  | User is redirected to a page saying you can only modify products if you are an admin them | Y |          |
| 7  | Visit the edit product url while not signed in as that user  | User is redirected to a page saying you can only modify products if you are an admin | Y |          |
| All Reviews Page  |                        |                  |      |             |
| 1        | Click on Add Review | Brings Add Review form if user is logged in | Y |          |
| 2        | My Account option displaye if not logged in | User is redirected to account page to login/register | Y |          |
| 3  | Click on the delete button as user or superuser  | Review is deleted | Y |          |
| 4  | Click on the edit button  | User or superuser is redirected to the edit Review page | Y |  Upon editing the comment the Review is updated        |
| 5  | Visit the delete review url while not signed in as that user  | User is redirected to a page saying you must be logged in | Y |          |
| 6  | Visit the edit review url while not signed in as that user  | User is redirected to a page saying you must be logged in | Y |          |
| 7  | Try to edit another users review  | User receives error message preventing them from doing so | Y |          |
| 8  | Try to delete another users review  | User receives error message preventing them from doing so | Y |          |
| Adding Reviews  |                        |                  |      |             |
| 1    | Fill out the add review form | All fields work as intended | Y | Validation is checked on submission       |
| 2    | Complete form without completing required fields | Validation error informs user to complete required fields | Y |          | 
| 3    | Add a review without being logged in | User redirected to login page | Y |          | 
| Editing Reviews  |                        |                  |      |             |
| 1    | Fill out the edit review form | All fields work as intended | Y | Validation is checked on submission       |
| 2    | User edits a review successfully | Review now requires approval by an admin | Y |          | 
| Contact Us Page  |                        |                  |      |             |
| 1        | Fill out the Contact Form | Form successfully submits if form passes validation | Y |          |
| 2        | Fill out the Contact Form | If form fails validation, neccessary messaging is provided for the customer to try again | Y |          |
| 3        | Fill out the Contact Form | Receive an email confirming that the form submission was received | Y |          |
| 4        | User fills out Contact Form | Admin receives email notifying them of the submission | Y |          |
| Site Messages  |                        |                  |      |             |
| 1        | Notification that something is successful or has failed | As you add/edit/delete or submit forms a message will appear top right of the site | Y |          |
| Admin Panel  |                        |                  |      |             |
| 1    | Open admin url while signed in as a regular user | User is informed they are not authorized and is prompted to sign in with a different account  | Y |          |
| 2    | Sign in as the superuser | Redirects user to the admin panel | Y |          |
| 3   | Click on any of the models in the admin panel | User sees a list of the objects with that model | Y |     |
| 4    | Click a specific object within the list of models  | User is shown the properties of that object | Y |  The user may modify, delete, or add objects from this page    |
| 5     | Click delete on an object | User is taken to delete confirmation page and upon confirmation receive a message at the top of the page | Y |   |
| 6     | Approve a user review | The review shows as approved and all site visitors can then view that review | Y |    |
| 7         | Unapprove a user review | The review can only be seen by the admin until the comment is reapproved | Y |          |
| 404 Page  |                        |                  |      |             |
| 9        | Enter an invalid url  | User redirected to a custom 404 error page | Y |          |
| Shopping Cart  |                        |                  |      |             |
| 1    | Click secure checkout or shopping cart icon  | Y | User is taken to Shopping Cart page | Y |          |
| 2   | User increases or decreases cart items | Quantity number reflects change | Y |     |
| 3   | User increases or decreases cart items and clicks Update | Quantity is updated and all pricing on cart page reflects the update | Y |     |
| 4   | User clicks remove | All products related to the remove button are removed | Y | This does not effect other item types in the cart if present    |
| 5    | Click secure checkout  | Y | Takes user to secure checkout page | Y |          |
| Payments  |                        |                  |      |             |
| 1    | Fill in information and submit form | Order is processed and user taken to success page if form is valid | Y |  All form validation functions correctly        |
| 2    | Click 'Save this delivery information to my profile' | Profile is updated with the new delivery information if new | Y |  This includes name and email       |
| 3    | Click 'Adjust Cart' button| User is redirected back to cart page | Y |  Can now make amendments to booking      |
| 4    | Click 'Complete Order' button | Order is processed and customer is directed to success page | Y |       |
| 5    | Click 'Complete Order' button 2 | Confirmation email received | Y |       |
| Success Page |                        |                  |      |             |
| 1    | User completed an order | All information relevant to their purchase is displayed | Y |       |
| My Profile Page |                        |                  |      |             |
| 1    | Click 'Update Information' after filling in the form | All information updates successfully if form is valid | Y |       |
| 2    | User profile information populated on checkout page | All information updated via profile page will be displayed on checkout if logged in | Y |       |
| 3    | Review Order History | All previous purchases are successfully shown | Y |       |
| 4    | Review Order History 2 | Redirected to success page for previous order and all details relating to that order is displayed | Y |       |
| Footer |                        |                  |      |             |
| 1    | Click on all Useful Links | Redirected to appropriate URL | Y |       |
| 2    | Click on all Social Media Links | Redirected to appropriate URL | Y |       |
| 3    | Subscribe to newsletter | Confirms successfully if valid email entered | Y |  connected to mailchimp and all appropriate messaging provided by them     |
| 4    | Click Privacy Policy | Redirected to privacy policy page with privacy policy information | Y |  This is an external URL and opens in new tab     |



## Bugs

- I had an issue with Heroku deployment. My Database did not migrate correctly. Luckily I still had all of my products and reviews on my local. So I researched how to loaddata onto a JSON file in order to migrate them across to my DB.

- I created the ability to do a sale on an item. I updated the product and product detail template. While the discounted price was showing, I then realised that the cart was not reflecting the same prices. I quickly dived into the cart code to add in the sale pricing logic.

- I had issues with template includes. I refactored the code in my cart but when I went to test this, I got an error straight away to tell me that product-images.html template I created did not exist. I knew it did exist. When I checked the include, it was set correctly. I dealt with Tutot support and we still couldn't find it. I realised then it was the second include URL that was causing the entire page to throw the error. I was wondering why it never had an issue with my cart-total.html include, since that would be rendered first if I had issues in my settings.py file, this would be a problem too. I then found the second URL and realised it was missing cart/ - {% include 'product-images.html' %} vs {% include 'cart/product-images.html' %}. Such as small issue can cause such a big problem!

- Added Defensive design for the backend of Reviews section. This introduced a new bug due to my initial Boolean logic. The Superuser was unable to edit or delete a review due to the boolean logic being no. I then updated the code to resolve this by specifying the users that can edit/delete in their own variable.




