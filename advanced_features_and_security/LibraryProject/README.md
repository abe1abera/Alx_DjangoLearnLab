# Advanced Features and Security - Permissions and Groups

## Custom Permissions
In `bookshelf/models.py`, the `Book` model defines custom permissions:
- `can_view` – Allows viewing books
- `can_create` – Allows creating new books
- `can_edit` – Allows editing existing books
- `can_delete` – Allows deleting books

## Groups
Using the Django Admin, create groups and assign permissions:
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → all permissions including `can_delete`

## Views
In `bookshelf/views.py`, views are protected with `@permission_required`:
- `view_books` → requires `can_view`
- `create_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`

## Testing
1. Create test users and assign them to groups.
2. Try accessing the views:
   - A Viewer can only see books.
   - An Editor can create/edit but not delete.
   - An Admin can do everything.



# Advanced Features and Security in Django

## Custom Permissions and Groups Setup

### Custom Permissions
We added the following permissions to the `Book` model (`bookshelf/models.py`):
- `can_create` → Allows users to create new books
- `can_edit` → Allows users to edit existing books
- `can_delete` → Allows users to delete books
- `can_view` → Allows users to view books

### Groups
We created the following groups via the Django Admin:
- **Viewers** → Has `can_view` permission
- **Editors** → Has `can_view`, `can_create`, and `can_edit` permissions
- **Admins** → Has all permissions including `can_delete`

### Permission Enforcement in Views
- In `bookshelf/views.py`, the `book_list` view is protected with:
  - `@login_required` → only authenticated users can access.
  - `@permission_required('bookshelf.view_book', raise_exception=True)` → user must have `view_book` permission.

### Testing Permissions
1. Create test users in the Django Admin.
2. Assign them to **Viewers**, **Editors**, or **Admins** groups.
3. Try accessing `/books/`:
   - Viewers can only view books.
   - Editors can add/edit but not delete.
   - Admins can perform all actions.

---

## Security Notes
- All database queries use Django ORM (no raw SQL).
- Templates include `{% csrf_token %}` for CSRF protection.
- Permissions are enforced at the view level for extra security.


