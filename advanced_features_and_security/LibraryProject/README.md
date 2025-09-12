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

