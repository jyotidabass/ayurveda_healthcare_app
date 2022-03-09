# Suprajā Abhiyān app
An Ayurvedic healthcare app focussed on prevention and management of chronic and critical non-communicable diseases (NCDs).

A public welfare initiative by [Rasāyu](https://app.rasayu.com/about-rasayu).

Currently a web app is under development with plans to develop mobile apps.
## Web app demo

Web app demo link: https://app.rasayu.com.

Steps for the demo developed so far:

1. Go to the [demo site](https://app.rasayu.com).
2. Click on the "Sign in" icon at the top right corner.
3. Sign in with the demo account credentials given, or create your user account
   as follows:
   1. Click on the "sign up" link in the sign in page that is displayed.
   2. Enter your email, username and password and click "Sign up".
   3. An email will be sent to the specified email ID for verification.
   4. Open the email and click on the verification link.
   5. Click on the "Sign in" icon again and sign in with your email and password.
4. Take your wellness assessment.
   1. On the welcome page, click on the "Assess your wellness" button.
   2. Click on the "Take your first assessment" link.
   3. Answer the wellness questionnaire and click "Submit".
   4. The answered questionnaire should now show up on the wellness assessment page with the date and score (higher is better) of the assessment. A date for the next follow up assessment is displayed below the questionnaire list.
   5. Below the questionnaires are shown the question-wise recommendations to be followed. Lower the score for a question, more strictly the corresponding recommendations are to be followed.

## Development setup

### Set `TokenAuthentication` for CRF RHC app API
RHC app API uses
[`TokenAuthentication`](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
for accessing CRF RHC app API. In the CRF project, create a token for a CRF
superuser or a user having the required permissions using Django management
command
[`drf_create_token`](https://www.django-rest-framework.org/api-guide/authentication/#using-django-managepy-command).
Set the generated token in `RHCAPP_AUTH_TOKEN` environment variable.

### Package changes

#### `django-adminlte3`

##### `adminlte3/templates/adminlte/lib/_main_header.html`

`webapp` overrides this template. Make following changes in this template:

1. Hide "messages" and "notifications" icons in the navbar for now.
   1. Add `{% block messages %}` to `<!-- Messages Dropdown Menu -->`.
   1. Add `{% block notifications %}` to `<!-- Notifications Dropdown Menu -->`.

2. Add `{% block nav_bar_left %}` to `<!-- Left navbar links -->`.
