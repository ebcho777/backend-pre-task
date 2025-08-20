from rest_framework import serializers
from ..models import Contact, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class ContactListSerializer(serializers.ModelSerializer):
    company_info = serializers.SerializerMethodField()
    labels = LabelSerializer(many=True, read_only=True)

    def get_company_info(self, obj):
        """회사와 직책을 '회사 (직책)' 형태로 조합하여 반환"""
        company = obj.company or ""
        job_title = obj.job_title or ""
        
        if company and job_title:
            return f"{company} ({job_title})"
        elif company:
            return company
        elif job_title:
            return f"({job_title})"
        return ""

    class Meta:
        model = Contact
        fields = [
            'id',
            'profile_photo_url',
            'name',
            'email',
            'phone_number',
            'company_info',
            'labels',
        ]


class ContactDetailSerializer(serializers.ModelSerializer):
    """
    연락처 '상세' 조회, '생성', '수정'을 위한 시리얼라이저
    """
    
    labels = serializers.ListField(
        child=serializers.CharField(max_length=100),
        write_only=True, # 쓰기(생성/수정) 시에만 사용
        required=False
    )
    
    labels_read = LabelSerializer(source='labels', many=True, read_only=True)


    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'phone_number', 'company', 'job_title', 
            'memo', 'profile_photo_url', 'address', 'birth_date', 'website', 
            'labels', # 쓰기용 필드
            'labels_read', # 읽기용 필드
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        labels_data = validated_data.pop('labels', [])
        
        contact = Contact.objects.create(**validated_data)
        
        for label_name in labels_data:
            Label.objects.create(contact=contact, name=label_name)
        return contact

    def update(self, instance, validated_data):
        """연락처 수정 시, 기존 라벨은 모두 지우고 새로운 라벨 목록으로 교체"""
        labels_data = validated_data.pop('labels', None)
        
        instance = super().update(instance, validated_data)

        if labels_data is not None:
            instance.labels.all().delete()
            for label_name in labels_data:
                Label.objects.create(contact=instance, name=label_name)
        
        return instance