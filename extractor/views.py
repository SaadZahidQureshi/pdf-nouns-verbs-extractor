from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .models import ExtractedData
from .serializers import ExtractedDataSerializer
import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

class ExtractedDataView(APIView):    
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        extracted_data = ExtractedData.objects.all()
        serializer = ExtractedDataSerializer(extracted_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        file = self.request.FILES.get('file')

        if not email or not file:
            return Response({'error': 'Email and file are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if ExtractedData.objects.filter(email=email).first() is not None:
                return Response({'email': 'This email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            pdf_document = fitz.open(stream=file.read(), filetype='pdf')
            text = ''
            for page in pdf_document:
                text += page.get_text()

            words = word_tokenize(text)
            stop_words = set(stopwords.words('english'))
            filtered_words = [w for w in words if w.lower() not in stop_words]
            pos_tags = nltk.pos_tag(filtered_words)

            nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
            verbs = [word for word, pos in pos_tags if pos.startswith('VB')]

            # Prepare the data for saving
            data = {
                'email': email,
                'nouns': nouns,
                'verbs': verbs
            }
            # Validate and save the data
            serializer = ExtractedDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'index.html')

