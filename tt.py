from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# تحميل ملف الإكسل (تأكد أن فيه عمود "كلمة السر")
df = pd.read_excel(r"C:\Users\moh\Desktop\school\mohh.xlsx")  # غيّر المسار إذا لزم

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        student_id = request.form['student_id'].strip()
        password = request.form['password'].strip()

        # البحث عن الطالب برقم الجلوس
        student_data = df[df['رقم الجلوس'].astype(str) == student_id]

        if student_data.empty:
            result = "رقم الجلوس غير موجود."
        else:
            row = student_data.iloc[0]
            if str(row['كلمة السر']).strip() != password:
                result = "كلمة السر غير صحيحة."
            else:
                # إذا تطابق رقم الجلوس وكلمة السر، نعرض النتيجة
                result = {
                    'الاسم': row['الاسم'],
                    'رقم الجلوس': row['رقم الجلوس'],
                    'القران الكريم': row['القران الكريم'],
                    'التربية الإسلامية': row['التربية الإسلامية'],
                    'اللغة العربية': row['اللغة العربية'],
                    'رياضيات': row['رياضيات'],
                    'علوم': row['علوم'],
                    'الاجتماعيات': row['الاجتماعيات'],
                    'المجموع': row['المجموع'],
                    'التقدير': row['التقدير']
                }

    return render_template('ttt.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
