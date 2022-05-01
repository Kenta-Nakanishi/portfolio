from django.shortcuts import render, redirect
from .models import indexModel
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


def indexView(request):
    index_models = indexModel.objects.all()

    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.author = request.user
            post.save()

            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            message = forms.cleaned_data['content']
            subject = 'お問い合わせありがとうございます。'
            contact = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。

                {name} 様

                お問い合わせありがとうございます。
                以下の内容でお問い合わせを受付いたしました。
                内容を確認させていただき、ご返信させていただきますので、少々お待ちください。

                ---------------
                ◆お名前
                {name}

                ◆メールアドレス
                {email}

                ◆メッセージ
                {message}
                ---------------

                ※This email is an automatic reply from the system.

                Dear {name}

                Thank you for your inquiry.
                We have received inquiries with the above contents.
                We will check the contents and reply to you, so please be patient.
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )
            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')
            return redirect('/index')
    else:
        forms = ContactForm

    return render(request, 'PortFolioApp/index.html',{
        'index_models': index_models,
        'forms': forms,
        })


