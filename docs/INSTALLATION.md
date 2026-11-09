# تثبيت Arabic spot

## عبر Skills CLI
```bash
npx skills add https://github.com/cj0rm/arabic-spot --skill arabic-spot -a codex
```

## التثبيت اليدوي في Codex
انسخ هذا المشروع إلى `~/.agents/skills/arabic-spot`، بحيث يقع `SKILL.md` مباشرة داخل المجلد.

```bash
git clone https://github.com/cj0rm/arabic-spot.git
cd arabic-spot
bash scripts/install.sh
```

لـ Windows PowerShell:
```powershell
.\scripts\install.ps1
```

## الاستخدام
```text
$arabic-spot اكتب قصيدة من أربعة أبيات في حب عُمان، ثم راجع وزنها.
```

## التحقق
```bash
python3 scripts/validate.py
```

## فحص الوزن بالبرنامج (اختياري)
تحتاج إلى Python ومكتبة `pyarud` منفصلة:
```bash
python3 -m pip install pyarud
python3 scripts/scan.py --sadr "إِذَا غَامَرْتَ فِي شَرَفٍ مَرُومِ" --ajuz "فَلَا تَقْنَعْ بِمَا دُونَ النُّجُومِ"
```
لا تتطلب المهارة Python أو pyarud لتعمل بصفتها إرشادات للوكيل. تحقق من نتائج العروض المشكوك فيها.