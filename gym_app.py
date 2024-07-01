from PyQt5 import QtWidgets, uic
import sys
from models import register_member, mark_attendance, check_due_fees, update_fee_due_date

class GymApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(GymApp, self).__init__()
        uic.loadUi('ui/gym_app.ui', self)

        # Connect buttons to functions
        self.registerButton.clicked.connect(self.register_member)
        self.attendanceButton.clicked.connect(self.mark_attendance)
        self.checkFeesButton.clicked.connect(self.check_due_fees)

    def register_member(self):
        name = self.nameInput.text()
        contact = self.contactInput.text()
        member_id = register_member(name, contact)
        self.statusLabel.setText(f"Member registered with ID: {member_id}")

    def mark_attendance(self):
        member_id = self.memberIdInput.text()
        mark_attendance(member_id)
        self.statusLabel.setText("Attendance marked")

    def check_due_fees(self):
        due_fees = check_due_fees()
        fee_message = "\n".join([f"Fee due for {name} on {due_date}" for name, due_date in due_fees])
        self.statusLabel.setText(fee_message)

app = QtWidgets.QApplication(sys.argv)
window = GymApp()
window.show()
app.exec_()
