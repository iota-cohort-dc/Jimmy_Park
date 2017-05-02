# <=========== Models.py practice ============>


# (blank=True, null=True)
# this allows blank and null value to exist even info is blank
# [[[[[[[[[[[[[[[[[[[[[Quotes]]]]]]]]]]]]]]]]]]]]]
# LoginReg ------------models.py------------
class UserManager(models.Manager):
    def validate(self,data,user_id):
        # login val logic
class Users(models.Model):
    # user_id  this is hidden
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    alias = models.CharField(max_length)
    date_of_birth = models.DateField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Quotes--------------models.py------------
class QuoteManager(models.Manager):
    def validate(self, data, user_id):
        # quote val logic
class Quotes(models.Model):
    # quote_id  this is hidden
    user_submitted = models.CharField(max_length=255)
    author_of_quote = models.CharField(max_length=255)
    quote_content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
class Favorites(models.Model):
    user_fav_quote = models.ForeignKey(Users, related_name="user_fav_quo")
    fav_quote_content  = models.ForeignKey(Quotes, related_name="fav_quote_cont")
    created_at = models.DateTimeField()
# Quotes--------------views.py------------
def index(request):
    content ={
        'user': User.objects.get(id=request.session['user_id']),
        'etc....'
    }
    return render(request,"####/index.html",context)
def addQuote(request):
    result = Quotes.objects.addNewQuote(request.POST,request.session['user_id'])
    if result[0]:
        return redirect(reverse("####:####"))
    else:
        for errs in result[1]:
            message.error(request,errs)
        return redirect("/")
def addFavorites(request):

    return render(request,"####/index.html")

# [[[[[[[[[[[[[[[[[[[[[Appointments]]]]]]]]]]]]]]]]]]]]]
# LoginReg-----------------models.py------------
class UserManager(models.Manager):
    def Validate(self,data):
        # login val logic
class User(models.Model):
# Appointments-------------models.py------------
import datetime
from date import datetime
from timezone_field import TimeZoneField
class AppointmentManager(models.Manager):
    def Validate(self,data,user_id):
        # appointment val logic
class Appointments(models.Model):
    # appointment_id  this is hidden
    task_content = models.TextField(max_length=1000)
    status = models.TextField(max_length=50)
    appointment_time = models.DateTime()
    models.TimeInput()
    models.TimeField()




# [[[[[[[[[[[[[[[[[[[[[[[[Friends]]]]]]]]]]]]]]]]]]]]]]]

# [[[[[[[[[[[[[[[[[[[[[[[[[Poke]]]]]]]]]]]]]]]]]]]]]]]]]

# [[[[[[[[[[[[[[[[[[[[[[[Wish List]]]]]]]]]]]]]]]]]]]]]]





#
