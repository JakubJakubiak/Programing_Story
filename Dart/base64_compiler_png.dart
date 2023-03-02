import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:io';
import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'dart:typed_data';
import 'package:path/path.dart' as path;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  dynamic _base64String;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  File? _imageFile;
  final ImagePicker _picker = ImagePicker();
  dynamic imagebytess;

  void _pickImageBase64() async {
    try {
      final XFile? image = await _picker.pickImage(source: ImageSource.gallery);
      if (image == null) return;

      Uint8List imagebytes = await image!.readAsBytes();
      String _base64String = base64.encode(imagebytes);

      final imageTemp = File(image.path);
      setState(() {
        this._imageFile = imageTemp;
        imagebytess = _base64String;
      });
    } on PlatformException catch (e) {
      if (kDebugMode) {
        print('error');
      }
    }
  }

  Future<void> sendPostRequest() async {
    String url = 'http://........:3000/test';

    Map<String, dynamic> data = {"name": imagebytess};

    try {
      final response = await http.post(
        Uri.parse(url),
        body: jsonEncode(data),
        headers: {'Content-Type': 'application/json'},
      );

      final responseData = jsonDecode(response.body);
      print(response.body);
      print(responseData);
    } catch (error) {
      print(error);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          _imageFile == null
              ? Container()
              : Image.file(
                  _imageFile!,
                  width: 250,
                  height: 500,
                ),
          ElevatedButton(
              onPressed: () {
                HapticFeedback.heavyImpact();
                _pickImageBase64();
              },
              child: Text("Pick Image Convert to base64")),
          ElevatedButton(
              onPressed: () {
                HapticFeedback.heavyImpact();
                sendPostRequest();
              },
              child: Text("post")),
          imagebytess == null
              ? Column()
              : Expanded(
                  child: SingleChildScrollView(
                  scrollDirection: Axis.vertical,
                  child: SingleChildScrollView(
                    child: Text('$imagebytess'),
                  ),
                ))
        ],
      ),
    );
  }
}
