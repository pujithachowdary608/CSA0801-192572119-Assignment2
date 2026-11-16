correct_otp = "4821"
attempts = 0
verified = False
while attempts < 3:
    otp = input("Enter OTP: ").strip()
    if otp == "":
        print("Blank entry. Try again; attempt not counted.")
        continue
    if otp == correct_otp:
        verified = True
        print("OTP verified successfully.")
        break
    attempts += 1
    print("Incorrect OTP. Attempts used:", attempts)
else:
    print("Account locked for 30 minutes.")
if verified:
    print("Access granted.")
