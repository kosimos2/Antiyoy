using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Menu_Start : MonoBehaviour
{
    // Start is called before the first frame update
    private Button button; // Добавляем поле для хранения компонента Button


    void Awake()
    {
        button = GetComponent<Button>(); // Получаем компонент Button
        button.onClick.AddListener(MouseClick); // Регистрируем обработчик события нажатия на кнопку

    }
    private void MouseClick()
    {
            
        Debug.Log("3");
        SceneManager.LoadScene("Game");
        Debug.Log("4");
        
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
