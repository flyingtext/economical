# 📝 Sign Up Page Specification

## Purpose
Allow new users to securely create an account on the Economical platform.

---

## Layout
- **Logo / Branding**
  - Top center placement
  - Link back to homepage

- **Sign Up Form**
  - Full Name (text input, required)
  - Email (text input, validation: must be unique & valid email format)
  - Password (password input, masked, with strength indicator)
  - Confirm Password (password input, must match)
  - Contact Info (optional, phone number or secondary email)
  - "Accept Terms and Privacy Policy" checkbox (required)
  - "Create Account" button (primary CTA)

- **Helper Links**
  - "Already have an account? Log in" → navigates to Login page

---

## States
- **Default**
  - Empty form fields
- **Validation Errors**
  - Invalid email format → inline error
  - Weak password (policy: min length 8, at least 1 number, 1 special character) → inline error
  - Password mismatch → inline error
  - Terms not accepted → disable "Create Account" button
- **Success**
  - Display message: "Please check your email to verify your account."
  - Redirect to Email Verification Pending screen
- **Failure**
  - Duplicate email → inline error message
  - Server error → banner error message

---

## Security
- All submissions via HTTPS
- Email verification required before login
- Passwords hashed & salted on server
- Rate limiting to prevent abuse

---

## Accessibility
- Clear password requirements visible before entry
- Keyboard navigation supported
- ARIA labels for inputs
- Error messages announced to screen readers
