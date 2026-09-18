import 'package:firebase_core/firebase_core.dart';

class FirebaseBootstrap {
  static Future<void> initialize() async {
    // Generated firebase_options.dart will be added after the Firebase
    // project is created and configured for com.dhaval.gsettestseries.
    await Firebase.initializeApp();
  }
}
