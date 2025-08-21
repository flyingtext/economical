# 🔑 Password Reset Page Specification

## Purpose
Allow users to securely reset their account password if they have forgotten it or wish to change it.

---

## Layout

### Step 1: Request Reset
- **Logo / Branding**
  - Top center placement
- **Form**
  - Email field (text input, validation: must be registered email)
  - "Send Reset Link" button (primary CTA)
- **Helper Links**
  - "Back to Login"
  - "Create new account"

### Step 2: Reset Link (Email)
- Email content:
  - Subject: "Economical Password Reset Request"
  - Body: Secure link with expiration (e.g., valid for 30 minutes)
  - Note: If user did not request, ignore email

### Step 3: New Password Entry
- **Form**
  - New Password (password input, strength indicator)
  - Confirm Password (must match)
  - "Reset Password" button (primary CTA)
- **Helper Links**
  - "Back to Login"

### Step 4: Success
- Confirmation message: "Your password has been successfully reset."
- Redirect to Login page

---

## States
- **Default**
  - Empty input fields
- **Validation Error**
  - Invalid email format → inline error
  - Email not registered → error message
  - Password too weak (policy: min 8 chars, 1 number, 1 special char) → inline error
  - Password mismatch → inline error
- **Loading**
  - Button shows spinner while request is processing
- **Success**
  - Step 1: "Check your email for reset instructions."
  - Step 3: Redirect to success screen

---

## Security
- One-time use reset tokens (expire after 30 minutes or first use)
- All submissions via HTTPS
- Reset token stored hashed in DB
- Reset link invalidated after password change
- Rate limiting for reset requests

---

## Accessibility
- Keyboard navigation (Tab order: Email → Button)
- Clear error messages
- ARIA labels for inputs
- High contrast compliant
