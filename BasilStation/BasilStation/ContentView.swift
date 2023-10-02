//
//  ContentView.swift
//  BasilStation
//
//  Created by Ole Rößler on 01.10.23.
//

import SwiftUI


struct ContentView: View {
    @StateObject var viewModel = ViewModel()
    @State var note_text: String = ""

    var body: some View {
        Button("Reload Comments"){
            viewModel.fetchAllWatering()
        }
        NavigationView{
            List{
                ForEach(viewModel.watered, id: \.self){ watered in
                    HStack{
                        Text("\(watered.id): \(watered.note_text)-> \(watered.watered_date)")
                            .bold()
                    }
                    .padding(3)
                }
            }
            .navigationTitle("Watered")
            .onAppear{
                viewModel.fetchAllWatering()
            }
        }
        TextField(
            "Write a comment",
            text: $note_text
        )
        Button("Click me "){
            viewModel.makeWateringPostRequest()
        }
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
