from rest_framework import serializers
from .models import Project, Pledge
from users.serializers import CustomUserSerializer

#every model requires a serializer to be created

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    #owner = serializers.CharField(max_length=200) - REMOVED and replaces with ReadOnlyField
    owner = serializers.ReadOnlyField(source='owner.id') #saves a query to database and when project is created, the logged in user will be the owner
    total = serializers.ReadOnlyField()

    amount_pledges = serializers.ReadOnlyField() # ****
    goal_vs_pledges = serializers.ReadOnlyField() #### can this be named differently



    def create(self, validated_data):
        return Project.objects.create(**validated_data) #### what does this do?

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
#this is a manual section, hence the fields need to be identified, rather than the below ProjectDetailSerializer (shorthand)
        read_only_fields = ['id', 'supporter']

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)