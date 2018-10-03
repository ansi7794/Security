# Cross-site Request Forgery (CSRF)

## No Defenses
Target: http://cs558web.bu.edu/project2/login with csrfdefense=0 and xssdefense=4

Solution: csrf1.html

## Token validation

Target: http://cs558web.bu.edu/project2/login with csrfdefense=1 and xssdefense=4

The server sets a cookie named csrf_token to a random 16-byte value and also includes this value as a hidden field in the login form. When the form is submitted, the server verifies that the client’s cookie matches the value in the form. This cookie is not session specific but it remains the same for a given IP, a given browser and a given time window.

To side-step this defense mechanism, we will be using the XSS attack. By first solving xss1.html, before proceeding with this part. Then we need to construct now a single HTML file that upon execution, first hijacks the cookie and then proceeds to log-in as “attacker” achieving the same effect as in no defense part

Solution: csrf2.html
