import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  // Create a list of todo items
  final List<String> todoItems = [];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Todo App',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Todo App'),
        ),
        body: Column(
          children: [
            // Display a text field for adding new todo items
            TextField(
              onSubmitted: (value) {
                // When the user submits the text field, add the new todo item to the list
                setState(() {
                  todoItems.add(value);
                });
              },
            ),
            // Display a list of todo items
            Expanded(
              child: ListView.builder(
                itemCount: todoItems.length,
                itemBuilder: (context, index) {
                  // For each todo item, display a row with the item and two buttons for editing and deleting
                  return Row(
                    children: [
                      Text(todoItems[index]),
                      IconButton(
                        // When the user taps the edit button, display a dialog for editing the todo item
                        onPressed: () async {
                          String editedItem = await showDialog(
                            context: context,
                            builder: (context) {
                              return AlertDialog(
                                title: Text('Edit Todo Item'),
                                content: TextField(
                                  initialValue: todoItems[index],
                                ),
                                actions: [
                                  FlatButton(
                                    child: Text('Save'),
                                    onPressed: () {
                                      Navigator.of(context).pop(
                                        // Return the edited todo item from the dialog
                                       
