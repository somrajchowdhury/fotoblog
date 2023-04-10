from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    help_text = 'Your password must contain at least an uppercase or' \
                ' lowercase letter.'

    def validate(self, password, user=None):
        if not any(char.is_alpha() for char in password):
            raise ValidationError(self.help_text,
                                  code='password_without_letter')

    def get_help_text(self):
        return self.help_text

class ContainsNumberValidator:
    help_text = 'Your password must contain at least one number.'

    def validate(self, password, user=None):
        if not any(char.is_digit() for char in password):
            raise ValidationError(self.help_text,
                                  code='password_without_number')

    def get_help_text(self):
        return self.help_text
