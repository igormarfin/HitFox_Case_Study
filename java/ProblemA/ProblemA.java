//package mypackage;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;  //notice javax
import javax.swing.JLabel;
import javax.swing.text.*;
import java.awt.event.*;    
import java.util.*;

//import com.mypackage.DivisorsHash;

public class ProblemA extends JFrame   implements ActionListener
{

     JPanel pane = new JPanel();
     JButton button = new JButton("Generate!");
     GridBagConstraints c = new GridBagConstraints();
     JTextField textField = new JTextField(100);
     JLabel label = new JLabel(convertToMultiline("Sollution of ProblemA:\n\n\n\n\n "));
   
    protected static final String textFieldString = "JTextField";
    String text;


  ProblemA() // the frame constructor method
  {
     

      super(" ProblemA ");
      setSize(1000,500);
      //setBounds(100,100,300,100);
   //     setLayout(new BorderLayout());
   pane.setLayout(new GridBagLayout());

    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container con = this.getContentPane(); // inherit main frame
    con.add(pane); // add the panel to frame
    // customize panel here
    // pane.add(someWidget);
  //  label.setVerticalTextPosition(JLabel.CENTER);
 //   label.setHorizontalTextPosition(JLabel.CENTER);
    button.requestFocus();
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 0;
    button.setMnemonic('G'); // associate hotkey to button
    button.addActionListener(this);
  
    pane.add(button, c);


    textField.setActionCommand(textFieldString);
    textField.addActionListener(this);

    textField.addKeyListener(new KeyAdapter() {

public void keyTyped(KeyEvent e) {
      char c = e.getKeyChar();


  if (!((c >= '0') && (c <= '9') || (c == ',') ||
     (c == KeyEvent.VK_BACK_SPACE) ||
        (c == KeyEvent.VK_DELETE))) {

      Toolkit.getDefaultToolkit().beep();
      
        e.consume();

  }

}
});


    c.fill=  GridBagConstraints.HORIZONTAL;
    c.gridx = 2;
    c.gridy = 0;
    c.ipadx = 0;
    c.weightx=3;
    c.anchor = GridBagConstraints.EAST; //to Right
    pane.add(textField,c);

    c.fill=  GridBagConstraints.CENTER;
    c.insets = new Insets(10,0,0,0);  //top padding
    c.ipady = 0;
    c.gridx = 1;       //aligned with button 2
    c.gridwidth = 2;   //2 columns wide
    c.gridy = 10;       //third row
    c.weighty = 10.0;   //request any extra vertical space
    c.anchor = GridBagConstraints.PAGE_END; //bottom of space
    pane.add(label,c);
    //con.add(label);
    //pack();
    setVisible(true); // display this frame
  }

  public int [] String2Int (String input) {

      ArrayList<String> list = new ArrayList<String>(Arrays.asList(input.split(",")));

      int [] results = new int[list.size()];

      Iterator<String> iterator = list.iterator();

      for (int i = 0; i < results.length; i++)

      {

         try {
             results[i] = Integer.parseInt(iterator.next());

         } catch (NumberFormatException nfe) {  System.out.println("Exception"); };



      }
  

      return results;
  }

  public String generate ( int [] keys){

      Arrays.sort(keys);
   
      String result="{ \n";
       for (int i = 0; i < keys.length; i++)
       {

      

                 DivisorsHash DH = new DivisorsHash(keys[i]);
                 DH.findDivisors();
      
                 result+=DH + ", \n " ;

       }
  


       result=result.substring(0, result.length()-2);
       result+="\n } ";
       return result;
  
  }

  public static String convertToMultiline(String orig)
{
    return "<html>" + orig.replaceAll("\n", "<br>");
}

  public void actionPerformed(ActionEvent e) {

      // if (e.getSource() == textField) {
      //              text = textField.getText();

      if (textFieldString.equals(e.getActionCommand())) {
            JTextField source = (JTextField)e.getSource();
            text= source.getText();
     
//            System.out.println(text);
            int [] keys =  String2Int (text);
            text = generate (keys);
            label.setText( convertToMultiline(text) );
        }

        else if(e.getSource() == button)
        {
          text =  textField.getText();
//          System.out.println(text);
          int [] keys =  String2Int (text);
          text = generate (keys);
          label.setText( convertToMultiline(text) );
   
        }
  
    }

  public static void main(String args[]) {

    SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                 //Turn off metal's use of bold fonts
        UIManager.put("swing.boldMetal", Boolean.FALSE);
    new ProblemA();


            }
        });

  }


}
