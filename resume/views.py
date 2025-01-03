from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string

# home
def home(request):
    return render(request, 'resume/home.html')



def about_us(request):
    return render(request, 'about.html')


# to call temp1
def temp1(request):
    return render(request, 'resume/temp1.html')

def temp3(request):
    return render(request, 'resume/temp3.html')

# to generate temp1
def generate_pdf(request):
    template_path = 'resume/resume_template.html'
    context = {
        'full_name': request.POST.get('full_name'),
        'address': request.POST.get('address'),
        'phone_number': request.POST.get('phone_number'),
        'email_address': request.POST.get('email_address'),
        'about_yourself': request.POST.get('about_yourself'),
        'experience': request.POST.get('experience'),
        'technical_skills': request.POST.get('technical_skills'),
        'soft_skills': request.POST.get('soft_skills'),
    }
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#to call temp 2
def temp2(request):
    return render(request, 'resume/temp2.html')

# to generate temp2
def generate_pdf2(request):
    if request.method == 'POST':
        template_path = 'resume/resume_temp2.html'
        context = {
            'full_name': request.POST['full_name'],
            'address': request.POST['address'],
            'phone_number': request.POST['phone_number'],
            'email_address': request.POST['email_address'],
            'skills':request.POST['skills'],
            'about_yourself': request.POST['about_yourself'],
            'experience': request.POST['experience'],
            'technical_skills': request.POST['technical_skills'],
            'soft_skills': request.POST['soft_skills'],
        }
        name=request.POST['full_name']
        # Create a Django template and render it to HTML
        template = get_template(template_path)
        html = template.render(context)

        # Create a PDF object and return it as response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="name.pdf"'

        # Convert HTML to PDF using xhtml2pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response
        )

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    return HttpResponse("Only POST requests are allowed")



def temp3(request):
    return render(request, 'resume/temp3.html')

def generate_pdf3(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        skills = [skill.strip() for skill in request.POST.get('skills', '').split(',')]

        # Retrieve dynamic education fields
        education = []
        education_count = int(request.POST.get('education_count', 0))
        for i in range(1, education_count + 1):
            degree = request.POST.get(f'education_degree_{i}')
            university = request.POST.get(f'education_university_{i}')
            year = request.POST.get(f'education_year_{i}')
            if degree and university and year:
                education.append({'degree': degree, 'university': university, 'year': year})

        # Retrieve dynamic experience fields
        experience = []
        experience_count = int(request.POST.get('experience_count', 0))
        for i in range(1, experience_count + 1):
            job_title = request.POST.get(f'experience_job_title_{i}')
            company = request.POST.get(f'experience_company_{i}')
            years = request.POST.get(f'experience_years_{i}')
            experience.append({'job_title': job_title, 'company': company, 'years': years})

        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'skills': skills,
            'education': education,
            'experience': experience,
        }

        # Generate PDF
        html = render_to_string('resume/resume_temp1.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generating PDF', status=500)

        return response

    return render(request, 'resume.temp3.html')


def temp4(request):
    return render(request, 'resume/templ2.html')

# def generate_pdf4(request):
#     if request.method == 'POST':
#         # Collect input data
#         name = request.POST.get('name', '')
#         title = request.POST.get('title', '')
#         email = request.POST.get('email', '')
#         phone = request.POST.get('phone', '')
#         profile = request.POST.get('profile', '')

#         education = request.POST.getlist('education')
#         experience = request.POST.getlist('experience')
#         skills = request.POST.get('skills', '')

#         context = {
#             'name': name,
#             'title': title,
#             'email': email,
#             'phone': phone,
#             'profile': profile,
#             'education': education,
#             'experience': experience,
#             'skills': skills,
#         }

#         # Generate PDF
#         html = render_to_string('/resume_templ2.html', context)
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'inline; filename="resume.pdf"'
#         pisa_status = pisa.CreatePDF(html, dest=response)

#         if pisa_status.err:
#             return HttpResponse('Error generating PDF', status=500)

#         return response
#     else:
#         return HttpResponse("Invalid request")


def generate_pdf4(request):
    if request.method == 'POST':
        # Collect input data
        name = request.POST.get('name', '')
        title = request.POST.get('title', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        profile = request.POST.get('profile', '')

        education = request.POST.getlist('education')
        experience = request.POST.getlist('experience')
        skills = request.POST.get('skills', '')

        # Convert skills to a list by splitting on commas
        skills_list = skills.split(',') if skills else []

        # Prepare context for rendering the template
        context = {
            'name': name,
            'title': title,
            'email': email,
            'phone': phone,
            'profile': profile,
            'education': education,
            'experience': experience,
            'skills_list': skills_list,  # Use the processed skills list
        }

        # Generate PDF
        html = render_to_string('resume/resume_templ2.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generating PDF', status=500)

        return response
    else:
        return HttpResponse("Invalid request")