
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST, require_GET
from django.utils import timezone
from .models import Post
from .forms import PostForm

# 1
def home(request):
    posts = Post.objects.filter(publicado=True).order_by('-creado')
    return render(request,'blog/home.html',{'posts':posts})

# 2
def saludo(request,nombre):
    return HttpResponse(f'Hola {nombre}')

# 3
def detalle_post(request,id):
    post = get_object_or_404(Post,id=id,publicado=True)
    return render(request,'blog/detalle.html',{'post':post})

# 4
def crear_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Post creado')
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'blog/crear.html',{'form':form})

# 5
def editar_post(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post actualizado')
            return redirect('detalle',id=id)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/editar.html',{'form':form})

# 6
def eliminar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    messages.warning(request,'Post eliminado')
    return redirect('home')

# 7
def buscar_post(request):
    q = request.GET.get('q','')
    posts = Post.objects.filter(titulo__icontains=q)
    return render(request,'blog/buscar.html',{'posts':posts,'q':q})

# 8
def posts_recientes(request):
    posts = Post.objects.order_by('-creado')[:5]
    return render(request,'blog/recientes.html',{'posts':posts})

# 9
def cambiar_estado(request,id):
    post = get_object_or_404(Post,id=id)
    post.publicado = not post.publicado
    post.save()
    return redirect('home')

# 10
def contar_posts(request):
    return HttpResponse(Post.objects.count())

# 11
def login_usuario(request):
    if request.method=='POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request,user)
            return redirect('home')
        messages.error(request,'Credenciales inválidas')
    return render(request,'auth/login.html')

# 12
def logout_usuario(request):
    logout(request)
    return redirect('login')

# 13
def registro_usuario(request):
    if request.method=='POST':
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        messages.success(request,'Usuario creado')
        return redirect('login')
    return render(request,'auth/registro.html')

# 14
@login_required
def perfil(request):
    return render(request,'auth/perfil.html')

# 15
@login_required
def dashboard(request):
    total = Post.objects.count()
    publicados = Post.objects.filter(publicado=True).count()
    return render(request,'admin/dashboard.html',{'total':total,'publicados':publicados})

# 16
def posts_json(request):
    data = list(Post.objects.values())
    return JsonResponse(data,safe=False)

# 17
def post_json(request,id):
    post = get_object_or_404(Post,id=id)
    return JsonResponse({'id':post.id,'titulo':post.titulo})

# 18
@require_POST
def crear_post_api(request):
    Post.objects.create(titulo=request.POST.get('titulo','Sin título'))
    return JsonResponse({'ok':True})

# 19
@require_POST
def eliminar_post_api(request,id):
    Post.objects.filter(id=id).delete()
    return JsonResponse({'deleted':True})

# 20
@require_GET
def total_posts_api(request):
    return JsonResponse({'total':Post.objects.count()})

# 21
def subir_imagen(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'blog/subir.html')

# 22
def galeria(request):
    posts = Post.objects.exclude(imagen='')
    return render(request,'blog/galeria.html',{'posts':posts})

# 23
def ver_imagen(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'blog/imagen.html',{'post':post})

# 24
def descargar_archivo(request,id):
    post = get_object_or_404(Post,id=id)
    return redirect(post.archivo.url)

# 25
def estadisticas(request):
    return render(request,'admin/stats.html',{
        'total':Post.objects.count(),
        'publicados':Post.objects.filter(publicado=True).count()
    })

# 26
def visitas(request,id):
    post = get_object_or_404(Post,id=id)
    post.visitas += 1
    post.save()
    return redirect('detalle',id=id)

# 27
def posts_por_autor(request,autor):
    posts = Post.objects.filter(autor__username=autor)
    return render(request,'blog/autor.html',{'posts':posts})

# 28
def posts_por_fecha(request,fecha):
    posts = Post.objects.filter(creado__date=fecha)
    return render(request,'blog/fecha.html',{'posts':posts})

# 29
def like_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.likes += 1
    post.save()
    return redirect('detalle',id=id)

# 30
def dislike_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.likes -= 1
    post.save()
    return redirect('detalle',id=id)

# 31
def posts_borrador(request):
    posts = Post.objects.filter(publicado=False)
    return render(request,'blog/borradores.html',{'posts':posts})

# 32
def publicar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.publicado = True
    post.publicado_en = timezone.now()
    post.save()
    return redirect('detalle',id=id)

# 33
def despublicar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.publicado = False
    post.save()
    return redirect('home')

# 34
def mis_posts(request):
    posts = Post.objects.filter(autor=request.user)
    return render(request,'blog/mis_posts.html',{'posts':posts})

# 35
def duplicar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.pk = None
    post.titulo += ' (copia)'
    post.save()
    return redirect('home')

# 36
def posts_populares(request):
    posts = Post.objects.order_by('-visitas')[:10]
    return render(request,'blog/populares.html',{'posts':posts})

# 37
def posts_sin_imagen(request):
    posts = Post.objects.filter(imagen='')
    return render(request,'blog/sin_imagen.html',{'posts':posts})

# 38
def posts_con_imagen(request):
    posts = Post.objects.exclude(imagen='')
    return render(request,'blog/con_imagen.html',{'posts':posts})

# 39
def limpiar_posts(request):
    Post.objects.all().delete()
    return redirect('home')

# 40
def posts_json_limit(request,limite):
    data = list(Post.objects.all()[:limite].values())
    return JsonResponse(data,safe=False)

# 41
def about(request):
    return render(request,'pages/about.html')

# 42
def contacto(request):
    if request.method=='POST':
        messages.success(request,'Mensaje enviado')
    return render(request,'pages/contacto.html')

# 43
def terms(request):
    return render(request,'pages/terms.html')

# 44
def privacy(request):
    return render(request,'pages/privacy.html')

# 45
def mantenimiento(request):
    return render(request,'errors/mantenimiento.html')

# 46
def error_404(request,exception=None):
    return render(request,'errors/404.html',status=404)

# 47
def sitemap(request):
    posts = Post.objects.filter(publicado=True)
    return render(request,'seo/sitemap.xml',{'posts':posts})

# 48
def robots(request):
    return render(request,'seo/robots.txt',content_type='text/plain')

# 49
def feed(request):
    posts = Post.objects.order_by('-creado')[:20]
    return render(request,'seo/feed.xml',{'posts':posts})

# 50
def healthcheck(request):
    return JsonResponse({'status':'ok'})
