// Cypress E2E tests for R8UC1, R8UC2, R8UC3 based on official requirements
// Requirements source: Requirements/Requirements (R8, R8UC1, R8UC2, R8UC3)
// Assumes the frontend is running at http://localhost:3000 and backend at http://localhost:5000

describe('R8 – Manipulate Todolist Associated with a Task', () => {
  let uid;
  let name;
  let email;
  const TODO_TEXT = 'Read Chapter 1';

  before(function () {
    // Create a fabricated user from a fixture
    cy.viewport(1920,1080);
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid;
          name = user.firstName + ' ' + user.lastName;
          email = user.email;
        });
      });
  });

  beforeEach(function () {
    // Log in before each test
    cy.viewport(1920,1080);
    cy.visit('http://localhost:3000');
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type(email);
    cy.get('form').submit();
    cy.get('h1').should('contain.text', 'Your tasks');
    // Navigate to the detail view of the first task (assume at least one exists)
    cy.contains('Tasks').click();    
  });

  after(function () {
    // Clean up by deleting the user from the database
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body);
    });
  });

  it('R8UC1: Add a New Todo Item (Main Scenario)', () => {
    cy.get('input[placeholder="Add a new todo item"]').as('todoInput');
    cy.get('@todoInput').type(TODO_TEXT);
    cy.contains('Add').should('not.be.disabled').click();
    cy.get('.todo-list .todo-item').last().should('contain', TODO_TEXT).and('not.have.class', 'done');
  });

  it('R8UC1: Add a New Todo Item (Alternative: Empty Description)', () => {
    cy.get('input[placeholder="Add a new todo item"]').as('todoInput');
    cy.contains('Add').should('be.disabled');
  });

it('RBUC2: Toggle a Todo Item (Active to done)', () => {


  // Add a new todo
  cy.get('input[placeholder="Add a new todo item"]').type(TODO_TEXT);
  cy.contains('Add').click();

  // Get the last todo item
  cy.get('.todo-list .todo-item').last().as('todoItem');

  // Click the checker to toggle the todo item
  cy.get('@todoItem').find('.checker').click();

  // Assert that the 'checked' class is added to the .checker span
  cy.get('@todoItem').find('.checker').should('have.class', 'checked');

  // Assert that the todo description has a line-through style
  cy.get('@todoItem').find('.editable')
    .should('have.css', 'text-decoration')
    .and('include', 'line-through');
});

it('R8UC2: Toggle a Todo Item (Done to Active)', () => {
  // Add a new todo
  cy.get('input[placeholder="Add a new todo item"]').type(TODO_TEXT);
  cy.contains('Add').click();

  // Get the last todo item
  cy.get('.todo-list .todo-item').last().as('todoItem');

  // Click the toggle element to mark as done
  cy.get('@todoItem').find('.checker').click();

  // Assert that the .checker span now has 'checked' class
  cy.get('@todoItem').find('.checker').should('have.class', 'checked');

  // Assert that the description has line-through
  cy.get('@todoItem').find('.editable')
    .should('have.css', 'text-decoration')
    .and('include', 'line-through');

  // Click again to unmark it (toggle back to active)
  cy.get('@todoItem').find('.checker').click();

  // Assert that 'checked' class is removed
  cy.get('@todoItem').find('.checker').should('not.have.class', 'checked');

  // Assert that text-decoration is gone
  cy.get('@todoItem').find('.editable')
    .should('have.css', 'text-decoration')
    .and('not.include', 'line-through');
});

it('R8UC3: Delete a Todo Item', () => {
  const TODO_TEXT = 'Buy groceries';

  // Add a new todo item
  cy.get('input[placeholder="Add a new todo item"]').type(TODO_TEXT);
  cy.contains('Add').click();

  // Get the last todo item
  cy.get('.todo-list .todo-item').last().as('todoItem');

  // Confirm the item exists before deletion
  cy.get('@todoItem').should('contain', TODO_TEXT);

  // Click the remover icon (×)
  cy.get('@todoItem').find('span.remover').click();

  // Optionally wait for DELETE request if needed
  // cy.wait('@deleteTodo'); // Uncomment if you're interceptting requests

  // Assert that the deleted item no longer exists in the list
  cy.get('.todo-list .todo-item').should('not.contain', TODO_TEXT);
});
});