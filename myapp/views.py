from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from myapp.models import EntryDoc, EntryProp, EntryUm
# from myapp.models import Dokumentasi, EntryDoc, EntryUm, Pengumuman

# Create your views here.
def index(request):
    context = {
        'page': 'Beranda',   
        'success': False,
        }    
    data = EntryDoc.objects.all()[:6]
    context['data'] = data 
    if request.method == 'POST':
        nama = request.POST['nama']
        nohp = request.POST['nohp']
        useremail = request.POST['email']
        subject = request.POST['jenis']
        message = request.POST['pesan'] + "\n identitas: \n" + "Nama: " + nama + ", No. HP: " + nohp
        email_from = useremail
        recipient_list = [settings.DEFAULT_EMAIL_RECEIVER,]
        send_mail( subject, message, email_from, recipient_list )
        context['success'] = True        
        return render(request, 'myapp/beranda.html', context)

    return render(request, 'myapp/beranda.html', context)

def dokumentasi(request):
    context = {
        'page': 'Dokumentasi',        
        }    
    data = EntryDoc.objects.all()    
    # for eachdata in data:
    #     print(eachdata.doc['picture'].url)
    #     print(type(eachdata.doc))        
    # context['data'] = data  
    paginator = Paginator(data, 3) # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj      
    return render(request, 'myapp/dokumentasi.html', context)

def pengajuan(request):
    context = {
        'page': 'Pengajuan',        
        }    
    data = EntryProp.objects.all()    
    # for eachdata in data:
    #     print(eachdata.id)
    #     print(type(eachdata))       
    # context['data'] = data
    paginator = Paginator(data, 3) # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'myapp/pengajuan.html', context)

def item(request, item_id):
    context = {
        'page': 'Proposal',        
        }    
    data = EntryProp.objects.get(id=item_id)    
    context['data'] = data.prop
    return render(request, 'myapp/item.html', context)

def pengumuman(request):
    context = {
        'page': 'Pengumuman',        
        }    
    data = EntryUm.objects.all()

    # context['data'] = data
    paginator = Paginator(data, 3) # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'myapp/pengumuman.html', context)

def contact(request):
    context = {
        'page': 'Hubungi',        
        }    
    return render(request, 'myapp/contact.html', context)

@login_required
def menu(request):
    context = {
        'page': 'Dashboard',       
        }    
    # form = DocumentForm()
    # context['form'] = form
    return render(request, 'myapp/admin-menu.html', context)

# auth
def user_login(request):
    if request.method == 'POST':
        context = {
        'page': 'Login',        
        } 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('myapp:menu')
            else:
                context['error'] = 'Your Account was Unactive'
                return render(request, 'myapp/beranda.html', context)
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            context['error'] = "Username/Password Incorrect"
            return render(request, 'myapp/beranda.html', context)        
    else:        
        return render(request, 'myapp/beranda.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))

@login_required
def up_dokumentasi(request):
    if request.method == 'POST' and request.FILES:
        pic = request.FILES['picture']  
        fs = FileSystemStorage()
        filename = fs.save(pic.name, pic)
        uploaded_file_url = fs.url(filename)              
        db = EntryDoc()                            
        db.doc = {
            'picture':request.FILES['picture']
            }
        db.save()     
        print(uploaded_file_url)                
        return redirect('myapp:dokumentasi')
    return redirect('myapp:menu')

@login_required
def up_proposal(request):
    if request.method == 'POST' and request.FILES:
        berkas = request.FILES['berkas'] 
        judul = request.POST['judul'] 
        desc = request.POST['keterangan']
        fs = FileSystemStorage()
        filename = fs.save(berkas.name, berkas)
        uploaded_file_url = fs.url(filename)              
        db = EntryProp()                            
        db.prop = {
            'file':berkas,
            'filename':judul,
            'description':desc
            }
        db.save()     
        print(uploaded_file_url)                
        return redirect('myapp:pengajuan')
    return redirect('myapp:menu')

@login_required
def up_pengumuman(request):
    if request.method == 'POST':   
        nama = request.POST['namaMasjid'] 
        tgl = request.POST['tgl'] 
        desc = request.POST['masjidketerangan']                 
        db = EntryUm()                            
        db.umum = {
            'nama':nama,
            'tanggal':tgl,
            'desc':desc
            }
        db.save()                          
        return redirect('myapp:pengumuman')
    return redirect('myapp:menu')