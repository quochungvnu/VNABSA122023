class InstructionsHandler:
    def __init__(self):
        self.ate = {}
        self.atsc = {}
        self.aspe = {}
        self.aooe = {}
        self.aope = {}
        self.aoste = {}
        self.joint = {}

    def load_instruction_set1(self, ):
        ################################# JOINT #################################

        self.joint['bos_instruct1'] = """Định nghĩa: Kết quả đầu ra sẽ bao gồm các khía cạnh (cả tiềm ẩn và rõ ràng) và hướng cảm xúc của các khía cạnh. Trong trường hợp không có bất kỳ khía cạnh nào, kết quả đầu ra sẽ là noaspectterm:none.
        Positive example 1-
        input: giao hàng nhanh. nhận đc áo đẹp hơn cả mong đợi! vải áo và đường may rất đẹp đóng gói rất xịn xò, đánh giá 5 sao lần sau sẽ mua ủng hộ shop tiếp ạ.
        output: Service:positive [SEP] General:positive
        Positive example 2-
        input: thấy giá rẻ, khá là đắn đo phân vân với sản phẩm khác. lựa chọn tới lui cuối cùng mua thử. thật đáng đồng tiền, vải mỏng mịn, k dày thô như mấy thun cá sấu khác, chất mát vô cùng. fom đẹp, size vừa vặn. chồng mình thử tới đâu khen tới đó. shop rất nhiệt tình, giao hàng siêu nhanh.
        output: Price:positive [SEP] Material:positive [SEP] Design:positive [SEP] Service:positive
        Negative example 1-
        input: chất liệu:vải mỏng màu sắc:trắng đúng không đúnh với mô tả sai kích cỡ.
        output: Material:negative [SEP] Service:negative
        Negative example 2-
        input: k to như mình nghĩ.
        output: Design:negative
        Neutral example 1-
        input: chất liệu bình thường đúng với mô tả:bình thường màu sắc bình thường hình ảnh chỉ mang tính chất nhận xu.
        output: Material:neutral [SEP] Design:neutral
        Neutral example 2-
        input: đúng với mô tả:ýe chất liệu bthg màu sắc:den.
        output: Material:neutral
        Bây giờ hoàn thành example sau-
        input: """

        self.joint['delim_instruct'] = ''
        self.joint['eos_instruct'] = ' \noutput:'

        ################################# ATE #################################

        self.ate['bos_instruct1'] = """Định nghĩa: Kết quả đầu ra sẽ bao gồm các khía cạnh (cả tiềm ẩn và rõ ràng) Đối với các trường hợp có các khía cạnh có ý kiến đi kèm được trích xuất từ văn bản đầu vào. Trong trường hợp không có khía cạnh, đầu ra sẽ là noaspectterm.
        Positive example 1-
        input: giao hàng nhanh. nhận đc áo đẹp hơn cả mong đợi! vải áo và đường may rất đẹp đóng gói rất xịn xò, đánh giá 5 sao lần sau sẽ mua ủng hộ shop tiếp ạ.
        output: giao hàng nhanh, áo đẹp hơn cả mong đợi
        Positive example 2-
        input: thấy giá rẻ, khá là đắn đo phân vân với sản phẩm khác. lựa chọn tới lui cuối cùng mua thử. thật đáng đồng tiền, vải mỏng mịn, k dày thô như mấy thun cá sấu khác, chất mát vô cùng. fom đẹp, size vừa vặn. chồng mình thử tới đâu khen tới đó. shop rất nhiệt tình, giao hàng siêu nhanh.
        output: thật đáng đồng tiền, vải mỏng mịn, fom đẹp, size vừa vặn, shop rất nhiệt tình, giao hàng siêu nhanh
        Bây giờ hoàn thành example sau-
        input: """

        self.ate['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) which have an associated opinion that are extracted from the input text. In cases where there are no aspects the output should be noaspectterm.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food, menu, service, setting
        Now complete the following example-
        input: """
        self.ate['delim_instruct'] = ''
        self.ate['eos_instruct'] = ' \noutput:'

        ################################# ATSC #################################

        self.atsc['bos_instruct1'] = """Định nghĩa: Kết quả đầu ra sẽ là 'positive' nếu aspect được xác định trong câu chứa một tình cảm tích cực. Nếu tình cảm của khía cạnh được xác định trong đầu vào là tiêu cực, câu trả lời sẽ là 'negative'. 
        Trong trường hợp khác, đầu ra nên là 'neutral'. Đối với các khía cạnh được phân loại là noaspectterm, tình cảm là 'none'.
        Ví dụ tích cực 1-
        input: giao hàng nhanh. nhận đc áo đẹp hơn cả mong đợi! vải áo và đường may rất đẹp đóng gói rất xịn xò, đánh giá 5 sao lần sau sẽ mua ủng hộ shop tiếp ạ. Khía cạnh là giao hàng nhanh.
        output: positive
        Ví dụ tích cực 2-
        input: chất liệu:cotton su đúng với mô tả:đúng màu sắc:màu nhạt hơn trên hình shipper thân thiện lắm vải ko mỏng lắm đâu hình ảnh mang tính chất nhận su. Khía cạnh là shipper thân thiện.
        output: positive
        Bây giờ hoàn thành example sau:-
        input: """
        
        self.atsc['bos_instruct2'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. 
        Otherwise, the output should be 'neutral'. For aspects which are classified as noaspectterm, the sentiment is none.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored. The aspect is menu.
        output: positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting. The aspect is food.
        output: positive
        Now complete the following example-
        input: """
        self.atsc['delim_instruct'] = ' Khía cạnh là '
        self.atsc['eos_instruct'] = '.\noutput:'

        ################################# ASPE #################################

        self.aspe['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:positive, 
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features:positive, iChat:positive, Photobooth:positive, garage band:positive
        Now complete the following example-
        input: """
        
        self.aspe['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu:positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food:positive, menu:positive, service:positive, setting:positive
        Now complete the following example-
        input: """
        self.aspe['delim_instruct'] = ''
        self.aspe['eos_instruct'] = ' \noutput:'

        ################################# AOOE #################################

        self.aooe['bos_instruct1'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. In cases where there are no aspects the output should be none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Now complete the following example-
        input: """
        
        self.aooe['bos_instruct2'] = """Definition: The output will be the opinion/describing word for the aspect term in the sentence. In cases where there are no aspects the output should be none.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery . The aspect term is delivery.
        output: rough
        Positive example 2- 
        input: At the end you 're left with a mild broth with noodles that you can slurp out of a cup . The aspect term is broth with noodles.
        output: mild
        Now complete the following example-
        input: """
        self.aooe['delim_instruct'] = ' The aspect is '
        self.aooe['eos_instruct'] = '.\noutput:'

        ################################# AOPE #################################

        self.aope['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) and the corresponding opinion/describing terms. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high, GUI:killer, applications:good, use:easy 
        Now complete the following example-
        input: """
        
        self.aope['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious, money:little
        Now complete the following example-
        input: """
        self.aope['delim_instruct'] = ''
        self.aope['eos_instruct'] = ' \noutput:'

        ################################# AOSTE #################################

        self.aoste['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) the corresponding opinion/describing terms and the sentiment polarity (positive, negative, neutral) of the opinion term . In cases where there are no aspects the output should be noaspectterm:none:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good:positive 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high:positive, GUI:killer:positive, applications:good:positive, use:easy:positive 
        Now complete the following example-
        input: """
        
        self.aoste['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) the corresponding opinion/describing terms and the sentiment polarity (positive, negative, neutral) of the opinion term . In cases where there are no aspects the output should be noaspectterm:none:none.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough:positive
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious:positive, money:little:positive
        Now complete the following example-
        input: """
        self.aoste['delim_instruct'] = ''
        self.aoste['eos_instruct'] = ' \noutput:'


    def load_instruction_set2(self, ):
        ################################# JOINT #################################

        self.joint['bos_instruct1'] = """Định nghĩa: Hãy trích xuất ra các khía cạnh và phân loại cảm xúc của các khía cạnh đó.
        Example 1-
        input: mua size m nhưng cảm thấy hơi bé một xíu, vải mát, đóng gói kĩ, đẹp
        output: Material:positive [SEP] Design:negative [SEP] Service:positive
        Example 2-
        input: Màu sắc:ngà ngà Áo tạm ổn phù hợp giá tiền nhưng khi nhận được áo thì phần ống tay bị mấy vệt đen ko biết có giặt ra đc không
        output: Design:negative [SEP] General:neutral [SEP] Price:positive 
        Now complete the following example-
        input: """

        self.joint['delim_instruct'] = ''
        self.joint['eos_instruct'] = ' \noutput:'

        ################################# ATE #################################

        self.ate['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) which have an associated opinion that are extracted from the input text. In cases where there are no aspects the output should be noaspectterm.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features, iChat, Photobooth, garage band
        Negative example 1-
        input: Speaking of the browser, it too has problems.
        output: browser
        Negative example 2-
        input: The keyboard is too slick.
        output: keyboard
        Neutral example 1-
        input: I took it back for an Asus and same thing- blue screen which required me to remove the battery to reset.
        output: battery
        Neutral example 2-
        input: Nightly my computer defrags itself and runs a virus scan.
        output: virus scan
        Now complete the following example-
        input: """
        
        self.ate['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) which have an associated opinion that are extracted from the input text. In cases where there are no aspects the output should be noaspectterm.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food, menu, service, setting
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it.
        output: toast, mayonnaise, bacon, ingredients, plate
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches.
        output: seats
        Neutral example 1-
        input: I asked for seltzer with lime, no ice.
        output: seltzer with lime
        Neutral example 2-
        input: They wouldnt even let me finish my glass of wine before offering another.
        output: glass of wine
        Now complete the following example-
        input: """
        self.ate['delim_instruct'] = ''
        self.ate['eos_instruct'] = ' \noutput:'

        ################################# ATSC #################################

        self.atsc['bos_instruct1'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. 
        Otherwise, the output should be 'neutral'. For aspects which are classified as noaspectterm, the sentiment is none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life. The aspect is battery life.
        output: positive
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!. The aspect is garage band.
        output: positive
        Negative example 1-
        input: Speaking of the browser, it too has problems. The aspect is browser.
        output: negative
        Negative example 2-
        input: The keyboard is too slick. The aspect is keyboard.
        output: negative
        Neutral example 1-
        input: I took it back for an Asus and same thing- blue screen which required me to remove the battery to reset. The aspect is battery.
        output: neutral
        Neutral example 2-
        input: Nightly my computer defrags itself and runs a virus scan. The aspect is virus scan.
        output: neutral
        Now complete the following example-
        input: """
        
        self.atsc['bos_instruct2'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. 
        Otherwise, the output should be 'neutral'. For aspects which are classified as noaspectterm, the sentiment is none.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored. The aspect is menu.
        output: positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting. The aspect is food.
        output: positive
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it. The aspect is toast.
        output: negative
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches. The aspect is seats.
        output: negative
        Neutral example 1-
        input: I asked for seltzer with lime, no ice. The aspect is seltzer with lime.
        output: neutral
        Neutral example 2-
        input: They wouldnt even let me finish my glass of wine before offering another. The aspect is glass of wine.
        output: neutral
        Now complete the following example-
        input: """
        self.atsc['delim_instruct'] = ' The aspect is '
        self.atsc['eos_instruct'] = '.\noutput:'

        ################################# ASPE #################################

        self.aspe['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:positive, 
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features:positive, iChat:positive, Photobooth:positive, garage band:positive
        Negative example 1-
        input: Speaking of the browser, it too has problems.
        output: browser:negative
        Negative example 2-
        input: The keyboard is too slick.
        output: keyboard:negative
        Neutral example 1-
        input: I took it back for an Asus and same thing- blue screen which required me to remove the battery to reset.
        output: battery:neutral
        Neutral example 2-
        input: Nightly my computer defrags itself and runs a virus scan.
        output: virus scan:neutral
        Now complete the following example-
        input: """
        
        self.aspe['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu:positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food:positive, menu:positive, service:positive, setting:positive
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it.
        output: toast:negative, mayonnaise:negative, bacon:negative, ingredients:negative, plate:negative
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches.
        output: seats:negative
        Neutral example 1-
        input: I asked for seltzer with lime, no ice.
        output: seltzer with lime:neutral
        Neutral example 2-
        input: They wouldnt even let me finish my glass of wine before offering another.
        output: glass of wine:neutral
        Now complete the following example-
        input: """
        self.aspe['delim_instruct'] = ''
        self.aspe['eos_instruct'] = ' \noutput:'

        ################################# AOOE #################################

        self.aooe['bos_instruct1'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. In cases where there are no aspects the output should be none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Negative example 1-
        input: One night I turned the freaking thing off after using it , the next day I turn it on , no GUI , screen all dark , power light steady , hard drive light steady and not flashing as it usually does . The aspect is GUI.
        output: no
        Negative example 2-
        input: I can barely use any usb devices because they will not stay connected properly . The aspect is usb devices.
        output: not stay connected properly
        Neutral example 1-
        input: However , the multi-touch gestures and large tracking area make having an external mouse unnecessary ( unless you 're gaming ) . The aspect is external mouse.
        output: unnecessary
        Neutral example 2-
        input: I wanted to purchase the extended warranty and they refused , because they knew it was trouble . The aspect is extended warranty.
        output: refused
        Now complete the following example-
        input: """

        self.aooe['bos_instruct2'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. In cases where there are no aspects the output should be none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Negative example 1-
        input: The menu is very limited - i think we counted 4 or 5 entrees . The aspect is menu.
        output: limited
        Negative example 2-
        input: The strong scents coming from the left and right of me negatively affected my taste buds . The aspect is scents.
        output: strong
        Neutral example 1-
        input: What came to our table was burned beyond recognition and stringy . The aspect is battery table.
        output: burned
        Neutral example 2-
        input: But , nothing stands out about the cooking . The aspect is cooking.
        output: nothing stands out
        Now complete the following example-
        input: """
        self.aooe['delim_instruct'] = ' The aspect is '
        self.aooe['eos_instruct'] = '.\noutput:'

        ################################# AOPE #################################

        self.aope['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) and the corresponding opinion/describing terms. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high, GUI:killer, applications:good, use:easy
        Negative example 1-
        input: A month or so ago , the freaking motherboard just died .
        output: motherboard:freaking, motherboard:freaking
        Negative example 2-
        input: I had always used PCs and been constantly frustrated by the crashing and the poorly designed operating systems that were never very intuitive .
        output: operating systems:poorly designed, operating systems:intuitive
        Neutral example 1-
        input: It has a 10 hour battery life when you 're doing web browsing and word editing , making it perfect for the classroom or office , and in terms of gaming and movie playing it 'll have a battery life of just over 5 hours .
        output: web browsing:perfect, word editing:perfect
        Neutral example 2-
        input: no complaints with their desktop , and maybe because it just sits on your desktop , and you do n't carry it around , which could jar the hard drive , or the motherboard .
        output: hard drive:jar, motherboard:jar
        Now complete the following example-
        input: """
        
        self.aope['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious, money:little
        Negative example 1-
        input: From the terrible service , to the bland food , not to mention the unaccommodating managers , the overall experience was horrible .
        output: service:terrible, food:bland, managers:unaccommodating
        Negative example 2- 
        input: I had the Pad Thai and the noodles were sticky .
        output: Pad Thai:sticky, noodles:sticky
        Neutral example 1-
        input: The Dim Sum was so-so , but not spectacular .
        output: Dim Sum:so-so, Dim Sum:not spectacular
        Neutral example 2- 
        input: The location and ambience is Ok but the food is what makes up for it .
        output: mlocationeal:Ok, ambience:Ok
        Now complete the following example-
        input: """
        self.aope['delim_instruct'] = ''
        self.aope['eos_instruct'] = ' \noutput:'

        ################################# AOSTE #################################

        self.aoste['bos_instruct1'] = """Definition: The output will be the aspects (both implicit and explicit) the corresponding opinion/describing terms and the sentiment polarity (positive, negative, neutral) of the opinion term . In cases where there are no aspects the output should be noaspectterm:none:none.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good:positive 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high:positive, GUI:killer:positive, applications:good:positive, use:easy:positive
        Negative example 1-
        input: A month or so ago , the freaking motherboard just died .
        output: motherboard:freaking:negative, motherboard:freaking:negative
        Negative example 2-
        input: I had always used PCs and been constantly frustrated by the crashing and the poorly designed operating systems that were never very intuitive .
        output: operating systems:poorly designed, operating systems:intuitive
        Neutral example 1-
        input: It has a 10 hour battery life when you 're doing web browsing and word editing , making it perfect for the classroom or office , and in terms of gaming and movie playing it 'll have a battery life of just over 5 hours .
        output: web browsing:perfect:neutral, word editing:perfect:neutral
        Neutral example 2-
        input: no complaints with their desktop , and maybe because it just sits on your desktop , and you do n't carry it around , which could jar the hard drive , or the motherboard .
        output: hard drive:jar:neutral, motherboard:jar:neutral
        Now complete the following example-
        input: """
        
        self.aoste['bos_instruct2'] = """Definition: The output will be the aspects (both implicit and explicit) the corresponding opinion/describing terms and the sentiment polarity (positive, negative, neutral) of the opinion term . In cases where there are no aspects the output should be noaspectterm:none:none.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough:positive
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious:positive, money:little:positive
        Negative example 1-
        input: From the terrible service , to the bland food , not to mention the unaccommodating managers , the overall experience was horrible .
        output: service:terrible:negative, food:bland:negative, managers:unaccommodating:negative
        Negative example 2- 
        input: I had the Pad Thai and the noodles were sticky .
        output: Pad Thai:sticky:negative, noodles:sticky:negative
        Neutral example 1-
        input: The Dim Sum was so-so , but not spectacular .
        output: Dim Sum:so-so:neutral, Dim Sum:not spectacular:neutral
        Neutral example 2- 
        input: The location and ambience is Ok but the food is what makes up for it .
        output: mlocationeal:Ok:neutral, ambience:Ok:neutral
        Now complete the following example-
        input: """
        self.aoste['delim_instruct'] = ''
        self.aoste['eos_instruct'] = ' \noutput:'