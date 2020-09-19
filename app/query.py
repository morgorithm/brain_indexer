from django.db.models import ObjectDoesNotExist
from django.db import IntegrityError
from .models import *

'''
1. 각 try-except에서 에러 발생 시 어떤 에러 발생하는지 확인
2. 없는 데이터를 가져오려 할 때 에러 발생하는지 보기
3. 로깅 추가하기

ObjectDoesNotExist : 없는 데이터를 조회한 경우
IntegrityError : Unique 설정한 데이터가 중복되는 경우
'''

class CategoryQuery(object) :
    def __init__(self) :
        pass

    def createCategory(self, name) :
        '''str => bool'''

        instance = Category(name=name)
        try :
            instance.save() # send SQL
            return True
        except IntegrityError : # name is duplicated
            return False

    def readCategory(self, name=None) :
        '''str(=None) => QuerySet'''

        if name is None :
            querySet = Category.objects.all()
        else :
            try :
                querySet = Category.objects.filter(name=name)
            except ObjectDoesNotExist :
                return None
        return querySet

    def updateCategory(self, oldName, newName) :
        '''str, str => bool'''

        try :
            querySet = Category.objects.filter(name=oldName).get()
        except ObjectDoesNotExist :
            return "{} Object Does Not Exist".format(oldName)
        
        querySet.name = newName
        try :
            querySet.save()
            return True
        except IntegrityError :
            return "{} is duplicated:{}".format("Category.name", newName)

    def deleteCategory(self, name) :
        '''str => bool'''
        
        try :
            querySet = Category.objects.get(name=name)
        except ObjectDoesNotExist :
            return "{} Object Does Not Exist".format(name)

        try :
            querySet.delete()
            return True
        except Exception as e : # 삭제시 발생할 오류가 있을까?
            print(e)
            return False

