class Payment_details:
    P_id = input("Enter payment id: 1345")
    Amount =input("Enter Amount:200")
    Acc_no =int(input("Enter acc_no"))
    p_status =input("payment_success")
    def getpayment_details(self):
        print("p_id:",self.p_id)
        print("Amount is:",self.Amount)
        print("Account num is:",self.Acc_no)
        print("payment status is:",self.P_status)

       