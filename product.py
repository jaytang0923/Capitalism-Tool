# -*- coding: utf-8 -*-
'''
File Name: product
Created on 2015年1月28日 下午1:15:14

@author: jay
'''
ProNames=(u"DVD",u"手机",u"摄像机",u"录像机",
          u"床",u"椅子",u"沙发",
          u"银项链",u"金戒指",
          u"皮包",u"皮带",u"皮箱",u"皮夹",
          u"照相机",u"相机胶卷",u"",u"",
          u"背包",u"高尔夫球杆",u"溜冰鞋",u"",
          u"台式电脑",u"笔记本电脑",u"掌上电脑",u"打印机",
          u"皮夹克",u"牛仔裤",u"汗衫",u"",
          u"便携游戏机",u"玩具车",u"玩具娃娃",u"电视游戏机",
          u"高级手表",u"运动手表",u"",u"",
          u"沐浴露",u"洗发水",u"肥皂",u"",
          u"瓶装牛奶",u"可乐",u"葡萄汁",u"葡萄酒",
          u"洗涤剂",u"牙膏",u"厕所清洗剂",u"",
          u"巧克力",u"饼干",u"水果糖",u"口香糖",
          u"蛋糕",u"冰激凌",u"酸奶",u"",
          u"眼睛膏",u"染发水",u"口红",u"香水",
          u"感冒药",u"咳嗽糖浆",u"头疼药",u"",
          u"空调",u"音响",u"微波炉",u"电视机",
          u"香烟",u"雪茄",u"",u"",
          u"面包",u"玉米罐头",u"罐装浓汤",u"玉米片",
          u"胶鞋",u"皮鞋",u"袜子",u"运动鞋子",
          u"汽车",u"摩托车",
          )

ProClass=(u"电子产品",u"家具",u"珠宝",u"皮具",u"摄影器材",u"体育用品",u"电脑",u"服装",u"玩具",u"表",u"沐浴用品",u"饮料",
    u"化工产品",u"零售",u"甜点",u"化妆品",u"药品",u"电器产品",u"烟草产品",u"主食",u"鞋类",u"汽车类")
AllProNames={
        ProClass[0]:(u"DVD",u"手机",u"摄像机",u"录像机"),
        ProClass[1]:(u"床",u"椅子",u"沙发"),
        ProClass[2]:(u"银项链",u"金戒指"),
        ProClass[3]:(u"皮包",u"皮带",u"皮箱",u"皮夹"),
        ProClass[4]:(u"照相机",u"相机胶卷"),
        ProClass[5]:(u"背包",u"高尔夫球杆",u"溜冰鞋"),
        ProClass[6]:(u"台式电脑",u"笔记本电脑",u"掌上电脑",u"打印机"),
        ProClass[7]:(u"皮夹克",u"牛仔裤",u"汗衫"),
        ProClass[8]:(u"便携游戏机",u"玩具车",u"玩具娃娃",u"电视游戏机"),
        ProClass[9]:(u"高级手表",u"运动手表"),
        ProClass[10]:(u"沐浴露",u"洗发水",u"肥皂"),
        ProClass[11]:(u"瓶装牛奶",u"可乐",u"葡萄汁",u"葡萄酒"),
        ProClass[12]:(u"洗涤剂",u"牙膏",u"厕所清洗剂"),
        ProClass[13]:(u"巧克力",u"饼干",u"水果糖",u"口香糖"),
        ProClass[14]:(u"蛋糕",u"冰激凌",u"酸奶"),
        ProClass[15]:(u"眼睛膏",u"染发水",u"口红",u"香水"),
        ProClass[16]:(u"感冒药",u"咳嗽糖浆",u"头疼药"),
        ProClass[17]:(u"空调",u"音响",u"微波炉",u"电视机"),
        ProClass[18]:(u"香烟",u"雪茄"),
        ProClass[19]:(u"面包",u"玉米罐头",u"罐装浓汤",u"玉米片"),
        ProClass[20]:(u"胶鞋",u"皮鞋",u"袜子",u"运动鞋子"),
        ProClass[21]:(u"汽车",u"摩托车"),
        }

"""
          AllProNames[ProClass[0]][0]:(((u"",),(u"",),(u"",)),),
          AllProNames[ProClass[0]][1]:(((u"",),(u"",),(u"",)),),
          AllProNames[ProClass[0]][2]:(((u"",),(u"",),(u"",)),),
          AllProNames[ProClass[0]][3]:(((u"",),(u"",),(u"",)),),
"""          
SubStuff={
          AllProNames[ProClass[0]][0]:(((u"电子元件",1),(u"铝",2)),),
          AllProNames[ProClass[0]][1]:(((u"电子元件",1),(u"塑料",1)),),
          AllProNames[ProClass[0]][2]:(((u"电子元件",1),(u"塑料",1),(u"玻璃",1)),),
          AllProNames[ProClass[0]][3]:(((u"电子元件",1),(u"玻璃",1),(u"钢",1)),),
          
          AllProNames[ProClass[1]][0]:(((u"木",80)),),
          AllProNames[ProClass[1]][1]:(((u"木",20),(u"纺织品",1)),),
          AllProNames[ProClass[1]][2]:(((u"木",30),(u"皮革",5),(u"棉花",5)),),
 
          AllProNames[ProClass[2]][0]:(((u"白银",3)),),
          AllProNames[ProClass[2]][1]:(((u"黄金",1)),),

          AllProNames[ProClass[3]][0]:(((u"皮革",5),(u"纺织品",1)),),
          AllProNames[ProClass[3]][1]:(((u"皮革",6),(u"钢",1)),),
          AllProNames[ProClass[3]][2]:(((u"皮革",5),(u"纺织品",1)),),
          AllProNames[ProClass[3]][3]:(((u"皮革",1)),),
          
          AllProNames[ProClass[4]][0]:(((u"电子元件",2),(u"玻璃",1),(u"塑料",1)),),
          AllProNames[ProClass[4]][1]:(((u"化工矿",5),(u"白银",1),(u"塑料",1)),),
          
          AllProNames[ProClass[5]][0]:(((u"聚酯",4),(u"亚麻布",1)),),
          AllProNames[ProClass[5]][1]:(((u"钢",1),(u"木",1)),),
          AllProNames[ProClass[5]][2]:(((u"皮革",2),(u"橡胶",1),(u"钢",1)),),
          
          AllProNames[ProClass[6]][0]:(((u"芯片",1),(u"电子元件",1),(u"钢",1)),),
          AllProNames[ProClass[6]][1]:(((u"芯片",2),(u"电子元件",1),(u"塑料",1)),),
          AllProNames[ProClass[6]][2]:(((u"芯片",3),(u"电子元件",1),(u"塑料",1)),),
          AllProNames[ProClass[6]][3]:(((u"电子元件",1),(u"塑料",2)),),
          
          AllProNames[ProClass[7]][0]:(((u"皮革",5),(u"纺织品",1)),),
          AllProNames[ProClass[7]][1]:(((u"纺织品",2),(u"染料",1)),),
          AllProNames[ProClass[7]][2]:(((u"羊毛",3),(u"染料",1)),),
          
          AllProNames[ProClass[8]][0]:(((u"电子元件",2),(u"塑料",2),(u"玻璃",1)),),
          AllProNames[ProClass[8]][1]:(((u"电子元件",1),(u"塑料",7)),),
          AllProNames[ProClass[8]][2]:(((u"纺织品",2),(u"棉花",2),(u"染料",1)),),
          AllProNames[ProClass[8]][3]:(((u"电子元件",1),(u"塑料",2)),),
          
          AllProNames[ProClass[9]][0]:(((u"玻璃",1),(u"钢",1)),),
          AllProNames[ProClass[9]][1]:(((u"电子元件",1),(u"塑料",4),(u"玻璃",1)),),
          
          AllProNames[ProClass[10]][0]:(((u"化工矿",1),(u"椰子油",1),(u"塑料",1)),),
          AllProNames[ProClass[10]][1]:(((u"化工矿",3),(u"塑料",1)),),
          AllProNames[ProClass[10]][2]:(((u"椰子油",1),(u"柠檬酸",1),(u"纸",1)),),
          
          AllProNames[ProClass[11]][0]:(((u"牛奶",2),(u"玻璃",1)),),
          AllProNames[ProClass[11]][1]:(((u"糖",5),(u"铝",1)),),
          AllProNames[ProClass[11]][2]:(((u"葡萄",10),(u"柠檬酸",1),(u"玻璃",1)),),
          AllProNames[ProClass[11]][3]:(((u"葡萄",5),(u"玻璃",1)),),
          
          AllProNames[ProClass[12]][0]:(((u"化工矿",3),(u"柠檬酸",),(u"塑料",)),),
          AllProNames[ProClass[12]][1]:(((u"化工矿",3),(u"塑料",)),),
          AllProNames[ProClass[12]][2]:(((u"化工矿",3),(u"塑料",)),),
          
          AllProNames[ProClass[13]][0]:(((u"可可",1),(u"牛奶",1)),),
          AllProNames[ProClass[13]][1]:(((u"面粉",9),(u"糖",1)),),
          AllProNames[ProClass[13]][2]:(((u"草莓",1)),),
          AllProNames[ProClass[13]][3]:(((u"玉米浆",1)),),
          
          AllProNames[ProClass[14]][0]:(((u"面粉",3),(u"鸡蛋",1),(u"可可",1)),),
          AllProNames[ProClass[14]][1]:(((u"牛奶",2),(u"草莓",2),(u"糖",1)),),
          AllProNames[ProClass[14]][2]:(((u"牛奶",2),(u"草莓",1),(u"柠檬酸",1)),),
          
          AllProNames[ProClass[15]][0]:(((u"化工矿",1),(u"塑料",1)),),
          AllProNames[ProClass[15]][1]:(((u"染料",2),(u"麦芽糖",1),(u"塑料",1)),),
          AllProNames[ProClass[15]][2]:(((u"染料",3),(u"麦芽糖",1),(u"塑料",1)),),
          AllProNames[ProClass[15]][3]:(((u"化工矿",1),(u"玻璃",1)),),
          
          AllProNames[ProClass[16]][0]:(((u"化工矿",1),(u"塑料",1)),),
          AllProNames[ProClass[16]][1]:(((u"化工矿",2),(u"塑料",1)),),
          AllProNames[ProClass[16]][2]:(((u"化工矿",2),(u"塑料",1)),),
          
          AllProNames[ProClass[17]][0]:(((u"钢",6),(u"电子元件",1)),),
          AllProNames[ProClass[17]][1]:(((u"电子元件",2),(u"钢",3),(u"铝",2)),),
          AllProNames[ProClass[17]][2]:(((u"电子元件",1),(u"玻璃",1),(u"塑料",1)),),
          AllProNames[ProClass[17]][3]:(((u"电子元件",3),(u"玻璃",2),(u"塑料",1)),),
          
          AllProNames[ProClass[18]][0]:(((u"烟草",1),(u"纸",1)),),
          AllProNames[ProClass[18]][1]:(((u"烟草",2),(u"纸",1)),),
          
          AllProNames[ProClass[19]][0]:(((u"面粉",9)),),
          AllProNames[ProClass[19]][1]:(((u"玉米",1)),),
          AllProNames[ProClass[19]][2]:(((u"冻鸡肉",1)),),
          AllProNames[ProClass[19]][3]:(((u"玉米",2),(u"糖",1)),),
          
          AllProNames[ProClass[20]][0]:(((u"橡胶",1)),),
          AllProNames[ProClass[20]][1]:(((u"皮革",5),(u"纺织品",1)),),
          AllProNames[ProClass[20]][2]:(((u"羊毛",1)),),
          AllProNames[ProClass[20]][3]:(((u"聚酯",2),(u"橡胶",1),(u"棉花",1)),),
          
          AllProNames[ProClass[21]][0]:(((u"引擎",1),(u"车身",1),(u"轮胎",4)),),
          AllProNames[ProClass[21]][1]:(((u"引擎",1),(u"钢",50),(u"轮胎",2)),),
          }

CLA=(u"电子产品",u"得多得多",u"weee")
TGOODS=(u"半成品",u"成品")
#name,(type,class,quality,demand,child)

class Product(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
    
    def selftest(self):
        print 'selftest'
        for pro in AllProducts:
            print "Product: %s"%pro#,type(AllProducts[pro]),len(AllProducts[pro])
            print "Type :",AllProducts[pro][0]
            print "Class :",AllProducts[pro][1]
            print "Quality : %d %d"%(AllProducts[pro][2],100-AllProducts[pro][2])
            
            print "Demand :",AllProducts[pro][3]
            
            print "need %d stuff:"%len(AllProducts[pro][4])
            stuff=AllProducts[pro][4]
            for i in range(len(stuff)):
                print "    %d %s"%(stuff[i][1],stuff[i][0])
                
            print '\n'
            
        print 'test new dict'
        for i in ProNames:
            ProDict[i]=i
            print i,len(ProDict),ProDict[i]
        
    
if __name__ == '__main__':
    print 'test'
    pro=Product('电视机')
    pro.selftest()
    print len(ProDict)
    print ProClass[3],AllProNames[ProClass[0]][0]
    print SubStuff[u"DVD"],len(SubStuff[u"DVD"])