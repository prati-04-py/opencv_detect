@api_view(['GET', 'POST'])
def drills(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':

        # snippets = Drill.objects.filter(drill_type='FREE')
        # serializer = DrillSerializer(snippets, many=True)
        # content = {'statuscode': 1, 'data': serializer.data, 'message': 'basic drills'}
        # return Response(content)
        snippets = Drill.objects.filter(drill_type='FREE')
        if request.GET.get("type")=="en": 
            # snippets = Drill.objects.filter(drill_type='FREE')
            serializer = DrillSerializer(snippets, many=True)
            content = {'statuscode': 1, 'data': serializer.data, 'message': 'basic drills'}
            return Response(content)
        elif request.GET.get("type")=="iw":
            
            # snippets = Drill.objects.filter(drill_type='FREE')
            serializer = DrillSerializerhebrew(snippets, many=True)
            content = {'statuscode': 1, 'data': serializer.data, 'message': 'basic drills'}
            return Response(content)

    elif request.method == 'POST':
        serializer = DrillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def adv_drills(request):
    """
    List all code snippets, or create a new snippet.
    """
    print(request.user)
    if request.user.is_authenticated:
        if request.method == 'GET':
            # snippets = Drill.objects.filter(drill_type='PAID').order_by('title')
            # object = Breath_count_test.objects.filter(user=request.user, is_passed=True)
            # print(object)
            # serializers = breath_test_count_serializerV(object, many=True)
            # serializer = DrillSerializer(snippets, many=True)
            # print('Data from serialzer', serializer.data)
            # testobj = Breath_timeset.objects.all()
            # serializer3 = Breath_timesetSerializer(testobj, many=True)
            # print("000000000000000000", serializer.data)
            # d = serializer.data
            # print('|||||||||||||||||||||||||||', d)

            # try:
            #     test = serializers.data[0]['is_passed']
            # except IndexError:
            #     test = False
            # content = {'statuscode': 1,
            #            'data': {'isTestPass': test, 'drill_data': serializer.data,
            #                     'test_drill': serializer3.data},
            #            'message': 'Advance Drill'}
            # return Response(content)
    # content = {'statuscode': 1, 'data': [], 'message': 'You are not Authorized'}
    # return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            if not request.GET.get("type") or request.GET.get("type")=="en":
                snippets = Drill.objects.filter(drill_type='PAID').order_by('title')
                object = Breath_count_test.objects.filter(user=request.user, is_passed=True)
                print(object)
                serializers = breath_test_count_serializerV(object, many=True)
                serializer = DrillSerializer(snippets, many=True)
                print('Data from serialzer', serializer.data)
                testobj = Breath_timeset.objects.all()
                serializer3 = Breath_timesetSerializer(testobj, many=True)
                print("000000000000000000", serializer.data)
                d = serializer.data
                print('|||||||||||||||||||||||||||', d)
            elif not request.GET.get("type") or request.GET.get("type")=="iw":
                snippets = Drill.objects.filter(drill_type='PAID').order_by('title')
                object = Breath_count_test.objects.filter(user=request.user, is_passed=True)
                print(object)
                serializers = breath_test_count_serializerV(object, many=True)
                serializer = DrillSerializerhebrew(snippets, many=True)
                print('Data from serialzer', serializer.data)
                testobj = Breath_timeset.objects.all()
                serializer3 = Breath_timesetSerializer(testobj, many=True)
                print("000000000000000000", serializer.data)
                d = serializer.data
                print('|||||||||||||||||||||||||||', d)

            try:
                test = serializers.data[0]['is_passed']
            except IndexError:
                test = False
            content = {'statuscode': 1,
                       'data': {'isTestPass': test, 'drill_data': serializer.data,
                                'test_drill': serializer3.data},
                       'message': 'Advance Drill'}
            return Response(content)
    content = {'statuscode': 1, 'data': [], 'message': 'You are not Authorized'}
    return Response(content, status=status.HTTP_401_UNAUTHORIZED)

