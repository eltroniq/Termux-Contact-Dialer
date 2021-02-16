# Termux-Contact-Dialer
Contact dialer for Termux written in Python. With Emoji support.
Useful if termux-contact-list returns empty.

### Setup
1. Export contacts via your contact app, should return a VCF file
2. Edit "contact_path" variable in "dialer.py" to your desired path.<br>Default: ```contact_path = "~/contacts.vcf"```
3. Make script executable: ```chmod +x dialer.py```
4. Set alias (in .aliases or .bashrc/.zshrc) like this:
```alias call="~/dialer.py"```

### Usage
```call contact_name```

automatically calls if only one match, returns a list with contacts and numbers if multiple matches, like this:

```
[0] contact 0: number 0
[1] contact 1: number 1
```

Type "1" and press return to call contact 1
