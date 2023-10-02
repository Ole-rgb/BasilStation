//
//  ViewModel.swift
//  BasilStation
//
//  Created by Ole Rößler on 02.10.23.
//

import Foundation
import SwiftUI

struct Watered: Hashable, Codable{
    let id: Int
    let note_text: String
    let watered_date: String
    
}

class ViewModel: ObservableObject{
    @Published var watered: [Watered] = []
    func fetchAllWatering(){
        guard let url = URL(string: "http://127.0.0.1:8000/api/v1/watering/") else{
            return
        }
        
        let task = URLSession.shared.dataTask(with: url){[weak self] data, _,
            error in
            guard let data = data, error == nil else{
                return
            }
            
            //Convert to json
            do{
                let watered = try JSONDecoder().decode([Watered].self, from: data)
                DispatchQueue.main.async{
                    self?.watered = watered
                }
            }
            catch{
                print(error)
            }
        }
        
        task.resume()
    }
    
    
    func makeWateringPostRequest(){
        guard let url = URL(string: "http://127.0.0.1:8000/api/v1/watering/") else{
            return
        }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let body: [String: AnyHashable] = [
            "note_text": "new message"
        ]
        
        request.httpBody = try? JSONSerialization.data(withJSONObject: body, options: .fragmentsAllowed)
        
        let task = URLSession.shared.dataTask(with: request){ data, _, error in
            guard let data = data, error == nil else{
                return
            }
            
            do{
                let response = try JSONSerialization.jsonObject(with: data, options: .fragmentsAllowed)
                print("SUCCESS: \(response)")

            }
            catch{
                print("SUCCESS:\(error)")
            }
        }
        task.resume()
    }
}

