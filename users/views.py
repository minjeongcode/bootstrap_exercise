from django.shortcuts               import render,redirect,HttpResponse
from django.contrib                 import auth
from django.contrib.auth.models     import User
from django.contrib.auth.hashers    import check_password
from django.contrib.auth            import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader         import render_to_string
from django.utils.http              import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding          import force_bytes, force_text
from django.core.mail               import EmailMessage

from users.tokens                   import account_activation_token

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username  = request.POST["username"],
                password  = request.POST["password1"],
                email     = request.POST["email"],
                last_name = request.POST["last_name"]
            )
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request) 
            message      = render_to_string('users/activation_email.html',{
                'user'  : user,
                'domain': current_site.domain,
                'uid'   : urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token' : account_activation_token.make_token(user),
            })
            mail_subject = "[Company Name] 회원가입 인증 메일입니다."
            user_email   = EmailMessage(mail_subject, message, to=[user.email])
            user_email.send()
            
            return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                '</div>'
            )
        return redirect('/users')
        
    return render(request, 'users/signup.html')

def activate(request, uid64, token):

    uid  = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        
        return redirect('/users')
    
    else:
        return HttpResponse('비정상적인 접근입니다.')
    
    
def login(request):
    return render(
        request,
        'users/login.html'
    )

# def signin(request):
#     pass

# def signup(request):
#     return render(
#         request,
#         'users/signup.html'
#     )