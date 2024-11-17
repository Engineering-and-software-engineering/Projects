import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Scanner;

class Product
{
	private int id;
	public String name; public double price; public int quantity;  

	Product( String new_name, double new_price, int new_quantity ) { name = new_name; price = new_price; quantity = new_quantity; }

	public int getID() { return id; }
	public void setID(int id) { id = id; }
}

class Inventory
{
	public Product[] products = new Product[2048];

	public double sumInventoryValue()
	{
		double value = 0.00d;

		int latestID = getLatestID();
		if (latestID >= 0) {
			for (int i = 0; i <= latestID; i++)
				value += products[i].price * products[i].quantity;
		}
		return value;
	}

	public int getLatestID()
	{
		for (int i = 0; i < products.length; i++) {
			if ( products[i] == null )
				return i-1;
		}
		return -1;
	}

	public void addProduct( String name, double price, int quantity )
	{
		Product newProduct = new Product( name, price, quantity );

		// get and set new product id by incrementing latest product id
		int newID = getLatestID() + 1;
		newProduct.setID(newID);

		// add new product to inventory
		products[newID] = newProduct;
	}

	public void printInventory()
	{
		int latestID = getLatestID();

		if (latestID >= 0) {
			System.out.println("\nInventory value: " + sumInventoryValue() + "\n");
			for (int i = 0; i <= latestID; i++) {
				System.out.println("Product #" + products[i].getID() + ": " + products[i].name);
				System.out.println("Price: " + products[i].price);
				System.out.println("Quantity: " + products[i].quantity + "\n");
			}
		}
	}

	public void stockProduct(int productID) { products[productID].quantity++; }
	public void destockProduct(int productID) { products[productID].quantity--; }
}

public class ProductInventory
{
	public static void main(String[] args) throws IOException
	{
		Inventory inv = new Inventory();
		Scanner scan = new Scanner(new InputStreamReader(System.in));

		String productName; double productPrice; int productQuantity;

		System.out.println("How many products would you like to add to the inventory? ");
		int numProducts = scan.nextInt(); scan.nextLine();

		for (int i = 0; i < numProducts; i++) {

			System.out.println("Enter a product name");
			productName = scan.nextLine();

			System.out.println("Enter a price for product: " + productName);
			productPrice = scan.nextDouble();

			System.out.println("Enter a quantity for product: " + productName);
			productQuantity = scan.nextInt(); scan.nextLine();

			inv.addProduct( productName, productPrice, productQuantity );

		}

		inv.printInventory();
		inv.destockProduct(0);
		inv.printInventory();
	}
}