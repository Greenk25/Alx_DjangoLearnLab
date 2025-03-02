## Permissions and Groups Setup

### Custom Permissions
Custom permissions are defined in the `Book` model:
- can_view: Can view book
- can_create: Can create book
- can_edit: Can edit book
- can_delete: Can delete book

### User Groups
Three user groups are created:
- Editors: Assigned `can_view` and `can_create` permissions.
- Viewers: Assigned `can_view` permission.
- Admins: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Enforcing Permissions in Views
Permissions are enforced in views using the `permission_required` decorator.

### Testing
Manually test by creating test users, assigning them to groups, and verifying access to various parts of the application.

