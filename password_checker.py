import math
import re
import sys
from zxcvbn import zxcvbn

def calculate_entropy(password):
    """
    حساب الإنتروبيا بناءً على طول كلمة المرور وحجم مجموعة الأحرف المستخدمة.
    Formula: entropy = len * log2(charset_size)
    """
    if not password:
        return 0
    
    charset_size = 0
    # التحقق من وجود حروف صغيرة، كبيرة، أرقام، ورموز لزيادة حجم مجموعة الأحرف
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'[0-9]', password): charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset_size += 33 
    
    if charset_size == 0: return 0
    
    # حساب الإنتروبيا باستخدام اللوغاريتم الأساس 2
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def detect_leet_speak(password):
    """
    اكتشاف استبدال Leet (مثل استبدال 'a' بـ '@' أو 's' بـ '5').
    """
    leet_map = {
        '@': 'a', '4': 'a',
        '3': 'e',
        '1': 'i', '!': 'i',
        '0': 'o',
        '5': 's', '$': 's',
        '7': 't', '+': 't'
    }
    
    found_leet = []
    for char in password:
        if char in leet_map:
            found_leet.append(f"'{char}' -> '{leet_map[char]}'")
    
    return found_leet

def get_user_tips(score, entropy, leet_found):
    """
    إنشاء نصائح باللغة الإنجليزية بناءً على نتائج التحليل.
    """
    tips = []
    if score < 3:
        tips.append("- Try to make the password longer (more than 12 characters).")
        tips.append("- Use a mix of uppercase, lowercase, numbers, and symbols.")
    
    if entropy < 50:
        tips.append("- Low entropy; the password might be easy to guess via brute force.")
        
    if leet_found:
        tips.append("- Leet speak substitutions are well-known to hackers; don't rely on them alone.")
        
    if score >= 3 and entropy >= 60:
        tips.append("- Very good password! Keep using complex passwords.")
        
    return tips

def check_password(pwd):
    """
    تحليل كلمة مرور واحدة وإرجاع النتائج.
    """
    # استخدام مكتبة zxcvbn للتحقق من القاموس والأنماط
    analysis = zxcvbn(pwd)
    
    entropy = calculate_entropy(pwd)
    leet_substitutions = detect_leet_speak(pwd)
    score = analysis['score'] # من 0 إلى 4
    
    score_labels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Strong", 4: "Very Strong"}
    
    return {
        "password": pwd,
        "score": score_labels[score],
        "entropy": entropy,
        "leet_detected": leet_substitutions,
        "patterns": [m['pattern'] for m in analysis['sequence']],
        "suggestions": analysis['feedback']['suggestions'],
        "user_tips": get_user_tips(score, entropy, bool(leet_substitutions))
    }

def print_report(r):
    """
    طباعة تقرير النتائج باللغة الإنجليزية.
    """
    print("\n" + "="*50)
    print(" PASSWORD ANALYSIS REPORT ")
    print("="*50)
    print(f"Password: {r['password']}")
    print(f"Strength: {r['score']}")
    print(f"Entropy:  {r['entropy']} bits")
    
    if r['leet_detected']:
        print(f"Leet Speak Detected: {', '.join(r['leet_detected'])}")
        
    if r['patterns']:
        # إزالة التكرار في الأنماط المكتشفة
        unique_patterns = list(set(r['patterns']))
        print(f"Detected Patterns: {', '.join(unique_patterns)}")
        
    if r['suggestions'] or r['user_tips']:
        print("\nTips & Recommendations:")
        # دمج الاقتراحات من المكتبة والنصائح المخصصة
        all_tips = r['suggestions'] + r['user_tips']
        for tip in all_tips:
            print(f"  * {tip}")
    
    print("="*50 + "\n")

def main():
    """
    الدالة الرئيسية لاستقبال مدخلات المستخدم.
    """
    print("Welcome to the Password Strength Checker!")
    print("Type 'exit' to quit the program.")
    
    while True:
        # استقبال كلمة المرور من المستخدم
        user_input = input("\nEnter a password to check: ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting... Stay safe!")
            break
            
        if not user_input:
            print("Please enter a valid password.")
            continue
            
        # تحليل كلمة المرور وطباعة التقرير
        result = check_password(user_input)
        print_report(result)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
