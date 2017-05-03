from django.core.mail import send_mass_mail
 
def sendMail(string):
    print 'send'
    message1 = ('hello aaaaaaaaa', 'Here is the messagesad fasdfasdfasdfasdf', 'hanshenghuijd@126.com', ['hanshenghui@jd.com', '362640516@qq.com'])
    message2 = ('hello 222222222', 'Here is another messagefsadfasdfasdfasdf', 'hanshenghuijd@126.com', ['hanshenghui@jd.com','hanshenghui@jd.com'])
    print send_mass_mail((message1,message2), fail_silently=True)
    #print send_mass_mail(message2, fail_silently=False)
    print 'doen'