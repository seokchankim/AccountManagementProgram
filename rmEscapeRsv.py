import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
import requests;
import sys;

def earthStarEscapeReserve(rsvDt):
    url = "http://www.roomlescape.com/rev.theme.time.php";

    payload = {"themeSeq":"6", "reservationDate":rsvDt};

    response = requests.post(url, data = payload);

    res = response.text;

    content = "";

    mailSendYn = False;

    for l in res.replace('\t','').replace('\n','').replace('=','').replace('data-timeseq','').replace('\'','').split('class'):
        a = l.split(" ");
        time = a[1][a[1].find(">")+1:a[1].find("<")];
        psblYn = a[0];
        if time != "" and (time[:2] == "15" or time[:2] == "16"):
            content += f"[룸엘이스케이프 홍대1호점] 퇴근길 [{time}] is {psblYn}\n\n";
            if (psblYn != "impossible"):
                mailSendYn = True;

    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
        if re.match(reg, addr):
            smtp.sendmail(my_account, to_mail, msg.as_string())
            print("정상적으로 메일이 발송되었습니다.")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오.")    

    
    content += "빠른예약 : http://www.roomlescape.com/home.php?go=rev.make&themeSeq=6";
        
    print(content);

    if mailSendYn == True:
        # smpt 서버와 연결
        gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
        gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
        smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

        # 로그인
        my_account = "tjrcks1022@gmail.com"
        my_password = "knix owdg arib cspj"
        smtp.login(my_account, my_password)

        # 메일을 받을 계정
        to_mail = "12160538@inha.edu"

        # 메일 기본 정보 설정
        msg = MIMEMultipart()
        msg["Subject"] = "[룸엘이스케이프 홍대1호점] 5월 18일 퇴근길 가능시간안내"  # 메일 제목
        msg["From"] = my_account
        msg["To"] = to_mail

        # 메일 본문 내용\
        content_part = MIMEText(content, "plain")
        msg.attach(content_part)

        # # 이미지 파일 추가
        # image_name = "test.png"
        # with open(image_name, 'rb') as file:
        #     img = MIMEImage(file.read())
        #     img.add_header('Content-Disposition', 'attachment', filename=image_name)
        #     msg.attach(img)

        # 받는 메일 유효성 검사 거친 후 메일 전송
        sendEmail(to_mail)

        # smtp 서버 연결 해제
        smtp.quit()
    else:
        print("\n[메일 미발송] 현재 예약가능한 시간이 없습니다.\n\n");
        
def roomEscapeReserve(rsvDt):
    url = f"https://xn--2e0b040a4xj.com/reservation?branch=4&theme=&date={rsvDt}";

    response = requests.request('GET', url);

    res = response.text;

    themes = res.split("body>")[1].split('<h2 class="ff-bhs pax3">');

    mailContent = "";

    sendMailYn = False;

    for i in range(1, 6):
        themeName = themes[i].split('<li class="pax3">')[0].split('<')[0];

        if (i == 2 or i == 5):
            for j in range(1, len(themes[i].split('<li class="pax3">'))):
                a = themes[i].split('<li class="pax3">')[j];
                status = a[a.find("<label>")+len("<label>"):a.find("</label>")];
                time = a[a.find('<span class="ff-bhs">')+len('<span class="ff-bhs">'):a.find("</span>")];

                if (time[:2] == "15" or time[:2] == "16"):
                    mailContent += f"[지구별방탈출 홍대라스트시티점] {themeName} [{time}] is {status}\n\n";
                    if "불가" not in status:
                        sendMailYn = True;

    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
        if re.match(reg, addr):
            smtp.sendmail(my_account, to_mail, msg.as_string())
            print("정상적으로 메일이 발송되었습니다.")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오.")

    mailContent += "빠른예약 : https://xn--2e0b040a4xj.com/reservation?branch=4&date=2024-05-18#list";

    print(mailContent);

    if sendMailYn == True:
        # smpt 서버와 연결
        gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
        gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
        smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

        # 로그인
        my_account = "tjrcks1022@gmail.com"
        my_password = "knix owdg arib cspj"
        smtp.login(my_account, my_password)

        # 메일을 받을 계정
        to_mail = "12160538@inha.edu"

        # 메일 기본 정보 설정
        msg = MIMEMultipart()
        msg["Subject"] = "[지구별방탈출 홍대라스트시티점] 5월 18일 문신, 섀도우 가능시간안내"  # 메일 제목
        msg["From"] = my_account
        msg["To"] = to_mail

        # 메일 본문 내용\
        content_part = MIMEText(mailContent, "plain")
        msg.attach(content_part)

        # # 이미지 파일 추가
        # image_name = "test.png"
        # with open(image_name, 'rb') as file:
        #     img = MIMEImage(file.read())
        #     img.add_header('Content-Disposition', 'attachment', filename=image_name)
        #     msg.attach(img)

        # 받는 메일 유효성 검사 거친 후 메일 전송
        sendEmail(to_mail)

        # smtp 서버 연결 해제
        smtp.quit()
    else:
        print("\n[메일 미발송] 현재 예약가능한 시간이 없습니다.\n\n");
        
def main():
    args = sys.argv;
    
    try:
        rsvDt = args[1];

        earthStarEscapeReserve(rsvDt);
        roomEscapeReserve(rsvDt);
    except:
        rsvDt = "2024-05-18";

        earthStarEscapeReserve(rsvDt);
        roomEscapeReserve(rsvDt);
        
if __name__ == "__main__":
    main();