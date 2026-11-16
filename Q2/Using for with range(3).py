correct_otp = "4821"
verified = False
for attempt in range(3):
    while True:
        otp = input("Enter OTP: ").strip()
        if otp == "":
            print("Blank entry. Try again; attempt not counted.")
            continue
        break
    if otp == correct_otp:
        verified = True
        print("OTP verified successfully.")
        break
    print("Incorrect OTP. Attempts used:", attempt + 1)
else:
    print("Account locked for 30 minutes.")
if verified:
    print("Access granted.")
