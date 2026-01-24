package com.app.cm;
import com.app.contactManager.ContactStore;

public class Main {
    public static void main(String[] args) {
        ContactStore store = new ContactStore();
        store.setLogListener(
                new LogListener() {
                    @Override
                    public void onMessageLogged(String message) {
                        System.out.println(message);
                    }
                }
    }
}
